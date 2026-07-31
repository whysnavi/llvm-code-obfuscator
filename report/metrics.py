import re
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

def count_instructions(ir_text):
    count = 0
    for line in ir_text.splitlines():
        s = line.strip()
        if s and not s.startswith('define') and s not in ('{', '}'):
            count += 1
    return count

def cyclomatic_complexity(ir_text):
    branches  = len(re.findall(r'\bbr\b', ir_text))
    functions = len(re.findall(r'\bdefine\b', ir_text))
    return branches - functions + 2 * functions

def byte_entropy(text):
    counts = Counter(text)
    total  = len(text)
    return round(-sum((c/total) * math.log2(c/total)
                      for c in counts.values() if c > 0), 3)

def obfuscation_score(orig_instr, obf_instr, orig_cc, obf_cc, orig_ent, obf_ent):
    instr_inc = ((obf_instr - orig_instr) / orig_instr * 100) if orig_instr > 0 else 0
    cc_inc    = ((obf_cc - orig_cc) / orig_cc * 100) if orig_cc > 0 else 0
    ent_inc   = ((obf_ent - orig_ent) / orig_ent * 100) if orig_ent > 0 else 0
    return round((instr_inc + cc_inc + ent_inc) / 3, 2)

def print_report(original, obfuscated, strategy, probabilities=None, chart_path="output/metrics.png"):
    orig_instr = count_instructions(original)
    obf_instr  = count_instructions(obfuscated)
    orig_cc    = cyclomatic_complexity(original)
    obf_cc     = cyclomatic_complexity(obfuscated)
    orig_ent   = byte_entropy(original)
    obf_ent    = byte_entropy(obfuscated)
    score      = obfuscation_score(orig_instr, obf_instr, orig_cc, obf_cc, orig_ent, obf_ent)

    instr_pct  = round((obf_instr - orig_instr) / orig_instr * 100, 1) if orig_instr > 0 else 0
    ent_pct    = round((obf_ent - orig_ent) / orig_ent * 100, 3) if orig_ent > 0 else 0

    print("\n" + "="*55)
    print("       OBFUSCATION METRICS REPORT")
    print("="*55)
    print(f"  Strategy applied   : {strategy}")
    print(f"  Instructions       : {orig_instr} → {obf_instr} (+{obf_instr - orig_instr}) [{instr_pct}%]")
    print(f"  Cyclomatic CC      : {orig_cc} → {obf_cc} (+{obf_cc - orig_cc})")
    print(f"  Entropy (bits)     : {orig_ent} → {obf_ent} (+{round(obf_ent - orig_ent, 3)}) [{ent_pct}%]")
    print(f"  Obfuscation Score  : {score}%")
    print("="*55)

    if probabilities:
        print("\n  ML Strategy Confidence:")
        for strat, prob in probabilities.items():
            bar = '█' * int(prob / 5)
            print(f"  {strat:<30} {prob:>5}%  {bar}")
        print()

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle(f'Obfuscation Metrics — {strategy}', fontsize=13)

    metrics = [
        ("Instructions",         orig_instr, obf_instr),
        ("Cyclomatic Complexity", orig_cc,    obf_cc),
        ("Entropy (bits)",       orig_ent,   obf_ent),
    ]

    for ax, (title, before, after) in zip(axes, metrics):
        bars = ax.bar(["Before", "After"], [before, after],
                      color=["#185FA5", "#534AB7"], width=0.5)
        pct = round((after - before) / before * 100, 1) if before > 0 else 0
        ax.set_title(f'{title}\n(+{pct}%)', fontsize=11)
        ax.set_ylim(0, max(before, after) * 1.5 if max(before, after) > 0 else 1)
        for bar, val in zip(bars, [before, after]):
            ax.text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + max(before, after) * 0.03,
                    str(val), ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    print(f"  Chart saved to     : {chart_path}")