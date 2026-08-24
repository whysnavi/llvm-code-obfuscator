import os
import glob
import subprocess
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from parser.ir_parser import IRParser
from obfuscation.control_flow import ControlFlowObfuscator
from obfuscation.instruction_sub import InstructionSubstitution
from obfuscation.string_encrypt import StringEncryptor
from ml.feature_extractor import FeatureExtractor
from ml.model import ObfuscationSelector
from report.metrics import (
    count_instructions,
    cyclomatic_complexity,
    byte_entropy,
    obfuscation_score,
)

st.set_page_config(page_title="Adaptive LLVM Code Obfuscator", page_icon=":shield:", layout="wide")

st.markdown(
    """
    <style>
    .badge {
        display: inline-block; padding: 4px 12px; border-radius: 14px;
        font-size: 12px; font-weight: 600; margin-right: 6px; margin-bottom: 6px;
    }
    .badge-purple { background: #EEEDFE; color: #534AB7; }
    .badge-blue   { background: #E6F1FB; color: #0C447C; }
    .badge-green  { background: #E1F5EE; color: #085041; }
    .flow-step {
        background: #F5F3FF; border: 1px solid #E0DBFA; border-radius: 10px;
        padding: 10px 14px; text-align: center; font-size: 13px; font-weight: 600;
        color: #534AB7;
    }
    .flow-arrow { text-align: center; font-size: 20px; color: #A79EE8; padding-top: 10px; }
    .metric-card {
        background: #F8F8FC; border: 1px solid #ECEAFB; border-radius: 12px;
        padding: 16px 18px; text-align: left;
    }
    .metric-card .label { font-size: 12px; color: #6B6B85; font-weight: 600; text-transform: uppercase; letter-spacing: .04em; }
    .metric-card .value { font-size: 26px; font-weight: 700; color: #1A1A2E; margin: 4px 0; }
    .metric-card .delta { font-size: 13px; color: #0F8A5F; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# Adaptive LLVM Code Obfuscation")
st.markdown("#### using Machine Learning")

st.markdown(
    """
    <span class="badge badge-purple">Published: IJRASET Vol. 14, April 2026</span>
    <span class="badge badge-blue">Random Forest Strategy Selection</span>
    <span class="badge badge-green">Live Demo</span>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "A Random Forest classifier analyzes LLVM IR structure and automatically selects "
    "the best obfuscation strategy: Control Flow Flattening, Instruction Substitution, "
    "String Encryption, or All Passes Combined, rather than applying one fixed transform "
    "to every program."
)

st.markdown(
    "[GitHub Repository](https://github.com/whysnavi/llvm-code-obfuscator) &nbsp;|&nbsp; "
    "[Published Paper (DOI)](https://doi.org/10.22214/ijraset.2026.79512)"
)

st.divider()

flow_labels = ["IR / C Input", "Feature\nExtraction", "ML Strategy\nSelection", "Obfuscation", "Metrics\nReport"]
flow_cols = st.columns([3, 1, 3, 1, 3, 1, 3, 1, 3])
for i, label in enumerate(flow_labels):
    with flow_cols[i * 2]:
        st.markdown(f'<div class="flow-step">{label}</div>', unsafe_allow_html=True)
    if i < len(flow_labels) - 1:
        with flow_cols[i * 2 + 1]:
            st.markdown('<div class="flow-arrow">→</div>', unsafe_allow_html=True)

st.divider()

sample_files = sorted(glob.glob("samples/*.ll"))
sample_names = [os.path.basename(f) for f in sample_files]

col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("1. Choose input")
    tab1, tab2, tab3 = st.tabs(["Sample program", "Paste LLVM IR", "Paste C code"])

    compile_error = None

    with tab1:
        chosen = st.selectbox("Sample program", sample_names, index=sample_names.index("hello.ll") if "hello.ll" in sample_names else 0)
        with open(os.path.join("samples", chosen), "r", encoding="utf-8") as f:
            sample_ir = f.read()
        st.code(sample_ir, language="llvm", line_numbers=True)

    with tab2:
        pasted_ir = st.text_area(
            "Paste LLVM IR (.ll) here",
            height=250,
            placeholder="define i32 @add(i32 %a, i32 %b) {\nentry:\n  %result = add i32 %a, %b\n  ret i32 %result\n}",
            key="ir_paste_area",
        )
        st.code(pasted_ir if pasted_ir else "// nothing loaded yet", language="llvm", line_numbers=True)

    with tab3:
        c_code = st.text_area(
            "Paste C code here",
            height=250,
            placeholder="int add(int a, int b) {\n    int result = a + b;\n    return result;\n}\n\nint main() {\n    return add(5, 3);\n}",
            key="c_code_area",
        )
        st.caption("Compiled to LLVM IR using `clang -S -emit-llvm` before running the obfuscation pipeline.")

        c_ir_text = ""
        if c_code.strip():
            os.makedirs("output", exist_ok=True)
            c_path = "output/_streamlit_input.c"
            ll_path = "output/_streamlit_input_from_c.ll"
            with open(c_path, "w", encoding="utf-8") as f:
                f.write(c_code)
            try:
                result = subprocess.run(
                    ["clang", "-S", "-emit-llvm", c_path, "-o", ll_path],
                    capture_output=True, text=True, timeout=20,
                )
                if result.returncode != 0:
                    compile_error = result.stderr
                else:
                    with open(ll_path, "r", encoding="utf-8") as f:
                        c_ir_text = f.read()
            except FileNotFoundError:
                compile_error = "clang is not available in this environment."
            except subprocess.TimeoutExpired:
                compile_error = "Compilation timed out."

        if compile_error:
            st.error(f"clang compilation failed:\n\n{compile_error}")
        elif c_ir_text:
            st.success("Compiled to LLVM IR successfully.")
            with st.expander("View generated LLVM IR"):
                st.code(c_ir_text, language="llvm", line_numbers=True)

      # Auto-detect which input to run: prefer compiled C, then pasted IR, then the sample.
    if c_ir_text.strip():
        ir_text = c_ir_text
        active_source_label = f"Compiled C code"
    elif pasted_ir.strip():
        ir_text = pasted_ir
        active_source_label = "Pasted LLVM IR"
    else:
        ir_text = sample_ir
        active_source_label = f"Sample program ({chosen})"

    st.caption(f"Will run on: **{active_source_label}**")
    run_clicked = st.button("Run Obfuscator", type="primary", use_container_width=True)

with col_right:
    st.subheader("2. Pipeline output")

    if run_clicked and ir_text.strip():
        os.makedirs("output", exist_ok=True)

        with st.status("Running pipeline...", expanded=True) as status:
            st.write("**[1/5] Parsing LLVM IR...**")
            tmp_path = "output/_streamlit_input.ll"
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write(ir_text)
            parser = IRParser(tmp_path)
            ir = parser.get_ir_text()
            st.write(f"Functions found: `{parser.get_functions()}`")
            st.write(f"Instructions: `{len(parser.get_instructions())}`")

            st.write("**[2/5] Extracting features...**")
            extractor = FeatureExtractor()
            features = extractor.extract(ir)
            st.json(features)

            st.write("**[3/5] ML model selecting strategy...**")
            selector = ObfuscationSelector()
            strategy = selector.predict(features)
            probabilities = selector.get_probabilities(features)
            st.success(f"Selected strategy: **{strategy}**")
            st.bar_chart(probabilities)

            st.write("**[4/5] Applying obfuscation...**")
            passes = {
                "Control Flow Flattening": ControlFlowObfuscator(),
                "Instruction Substitution": InstructionSubstitution(),
                "String Encryption": StringEncryptor(),
            }
            if strategy == "All Passes Combined":
                obfuscated = ControlFlowObfuscator().obfuscate(ir)
                obfuscated = InstructionSubstitution().obfuscate(obfuscated)
                obfuscated = StringEncryptor().obfuscate(obfuscated)
            else:
                obfuscated = passes[strategy].obfuscate(ir)

            st.write("**[5/5] Generating metrics report...**")
            orig_instr = count_instructions(ir)
            obf_instr = count_instructions(obfuscated)
            orig_cc = cyclomatic_complexity(ir)
            obf_cc = cyclomatic_complexity(obfuscated)
            orig_ent = byte_entropy(ir)
            obf_ent = byte_entropy(obfuscated)
            score = obfuscation_score(orig_instr, obf_instr, orig_cc, obf_cc, orig_ent, obf_ent)

            status.update(label="Pipeline complete!", state="complete", expanded=False)

        instr_pct = round((obf_instr - orig_instr) / orig_instr * 100, 1) if orig_instr > 0 else 0
        cc_delta = obf_cc - orig_cc
        ent_pct = round((obf_ent - orig_ent) / orig_ent * 100, 3) if orig_ent > 0 else 0

        mc1, mc2, mc3, mc4 = st.columns(4)
        card_data = [
            (mc1, "Instructions", f"{orig_instr} → {obf_instr}", f"↑ +{instr_pct}%"),
            (mc2, "Cyclomatic CC", f"{orig_cc} → {obf_cc}", f"↑ +{cc_delta}"),
            (mc3, "Entropy (bits)", f"{orig_ent} → {obf_ent}", f"↑ +{ent_pct}%"),
            (mc4, "Obfuscation Score", f"{score}%", "&nbsp;"),
        ]
        for col, label, value, delta in card_data:
            with col:
                st.markdown(
                    f"""<div class="metric-card">
                    <div class="label">{label}</div>
                    <div class="value">{value}</div>
                    <div class="delta">{delta}</div>
                    </div>""",
                    unsafe_allow_html=True,
                )

        st.markdown("&nbsp;")

        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        fig.patch.set_facecolor("#FFFFFF")
        fig.suptitle(f"Obfuscation Metrics: {strategy}", fontsize=13)
        metrics = [
            ("Instructions", orig_instr, obf_instr),
            ("Cyclomatic Complexity", orig_cc, obf_cc),
            ("Entropy (bits)", orig_ent, obf_ent),
        ]
        for ax, (title, before, after) in zip(axes, metrics):
            bars = ax.bar(["Before", "After"], [before, after], color=["#185FA5", "#534AB7"], width=0.5)
            pct = round((after - before) / before * 100, 1) if before > 0 else 0
            ax.set_title(f"{title}\n(+{pct}%)", fontsize=11)
            ax.set_ylim(0, max(before, after) * 1.5 if max(before, after) > 0 else 1)
            for bar, val in zip(bars, [before, after]):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(before, after) * 0.03,
                         str(val), ha="center", fontsize=10)
        plt.tight_layout()
        st.pyplot(fig)

        st.write("**Obfuscated LLVM IR output**")
        st.code(obfuscated, language="llvm", line_numbers=True)
        st.download_button("Download obfuscated .ll", obfuscated, file_name="obfuscated.ll")

    elif run_clicked:
        st.warning("Please provide some LLVM IR or C code first.")
    else:
        st.info("Choose a sample, paste IR, or paste C code, then click **Run Obfuscator**.")

st.divider()
st.caption(
    "Built by Vaishnavi Logishetty · "
    "[GitHub](https://github.com/whysnavi) · "
    "[LinkedIn](https://www.linkedin.com/in/vaishnavi-logishetty-501619336/)"
)
