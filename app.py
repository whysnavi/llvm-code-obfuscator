import os
import glob
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

st.set_page_config(page_title="Adaptive LLVM Code Obfuscator", page_icon="🛡️", layout="wide")

st.title("🛡️ Adaptive LLVM Code Obfuscation using Machine Learning")
st.caption(
    "A Random Forest classifier analyzes LLVM IR structure and automatically selects "
    "the best obfuscation strategy — Control Flow Flattening, Instruction Substitution, "
    "String Encryption, or All Passes Combined. Published in IJRASET, Vol. 14, Issue IV, "
    "April 2026."
)

st.markdown(
    "🔗 [GitHub Repository](https://github.com/whysnavi/llvm-code-obfuscator) &nbsp;|&nbsp; "
    "📄 [Published Paper (DOI)](https://doi.org/10.22214/ijraset.2026.79512)"
)

st.divider()

# --- Sample selection ---
sample_files = sorted(glob.glob("samples/*.ll"))
sample_names = [os.path.basename(f) for f in sample_files]

col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("1. Choose input")
    mode = st.radio("Input source", ["Pick a sample", "Paste your own LLVM IR"], horizontal=True)

    if mode == "Pick a sample":
        chosen = st.selectbox("Sample program", sample_names, index=sample_names.index("hello.ll") if "hello.ll" in sample_names else 0)
        with open(os.path.join("samples", chosen), "r", encoding="utf-8") as f:
            ir_text = f.read()
    else:
        ir_text = st.text_area(
            "Paste LLVM IR (.ll) here",
            height=250,
            placeholder="define i32 @add(i32 %a, i32 %b) {\nentry:\n  %result = add i32 %a, %b\n  ret i32 %result\n}",
        )

    st.code(ir_text if ir_text else "// nothing loaded yet", language="llvm", line_numbers=True)
    run_clicked = st.button("▶ Run Obfuscator", type="primary", use_container_width=True)

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

        m1, m2, m3, m4 = st.columns(4)
        instr_pct = round((obf_instr - orig_instr) / orig_instr * 100, 1) if orig_instr > 0 else 0
        ent_pct = round((obf_ent - orig_ent) / orig_ent * 100, 3) if orig_ent > 0 else 0
        m1.metric("Instructions", f"{orig_instr} → {obf_instr}", f"+{instr_pct}%")
        m2.metric("Cyclomatic CC", f"{orig_cc} → {obf_cc}", f"+{obf_cc - orig_cc}")
        m3.metric("Entropy (bits)", f"{orig_ent} → {obf_ent}", f"+{ent_pct}%")
        m4.metric("Obfuscation Score", f"{score}%")

        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        fig.suptitle(f"Obfuscation Metrics — {strategy}", fontsize=13)
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
        st.download_button("⬇ Download obfuscated .ll", obfuscated, file_name="obfuscated.ll")

    elif run_clicked:
        st.warning("Please provide some LLVM IR first.")
    else:
        st.info("Choose a sample or paste your own IR, then click **Run Obfuscator**.")

st.divider()
st.caption(
    "Built by Vaishnavi Logishetty · "
    "[GitHub](https://github.com/whysnavi) · "
    "[LinkedIn](https://www.linkedin.com/in/vaishnavi-logishetty-501619336/)"
)
