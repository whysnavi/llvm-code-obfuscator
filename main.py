import os
import sys
from parser.ir_parser               import IRParser
from obfuscation.control_flow       import ControlFlowObfuscator
from obfuscation.instruction_sub    import InstructionSubstitution
from obfuscation.string_encrypt     import StringEncryptor
from ml.feature_extractor           import FeatureExtractor
from ml.model                       import ObfuscationSelector
from report.metrics                 import print_report

os.makedirs("output", exist_ok=True)

INPUT_FILE  = sys.argv[1] if len(sys.argv) > 1 else "samples/hello.ll"
base_name   = os.path.splitext(os.path.basename(INPUT_FILE))[0]
OUTPUT_FILE = f"output/{base_name}_obfuscated.ll"
CHART_FILE  = f"output/{base_name}_metrics.png"

print("\n" + "="*55)
print("   LLVM OBFUSCATOR WITH ADAPTIVE ML FRAMEWORK")
print("="*55)
print(f"\n   Input file: {INPUT_FILE}")

print("\n[1/5] Parsing LLVM IR...")
parser = IRParser(INPUT_FILE)
ir     = parser.get_ir_text()
print(f"      Functions found  : {parser.get_functions()}")
print(f"      Basic blocks     : {parser.get_basic_blocks()}")
print(f"      Instructions     : {len(parser.get_instructions())}")

print("\n[2/5] Extracting features...")
extractor = FeatureExtractor()
features  = extractor.extract(ir)
for k, v in features.items():
    print(f"      {k:<18} : {v}")

print("\n[3/5] ML model selecting strategy...")
selector      = ObfuscationSelector()
strategy      = selector.predict(features)
probabilities = selector.get_probabilities(features)
print(f"      Selected strategy: {strategy}")
print("\n      Confidence scores:")
for strat, prob in probabilities.items():
    bar = '█' * int(prob / 5)
    print(f"      {strat:<30} {prob:>5}%  {bar}")

print("\n[4/5] Applying obfuscation...")
passes = {
    "Control Flow Flattening" : ControlFlowObfuscator(),
    "Instruction Substitution": InstructionSubstitution(),
    "String Encryption"       : StringEncryptor(),
}

if strategy == "All Passes Combined":
    obfuscated = ControlFlowObfuscator().obfuscate(ir)
    obfuscated = InstructionSubstitution().obfuscate(obfuscated)
    obfuscated = StringEncryptor().obfuscate(obfuscated)
else:
    obfuscated = passes[strategy].obfuscate(ir)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(obfuscated)
print(f"      Output written to: {OUTPUT_FILE}")

print("\n[5/5] Generating metrics report...")
print_report(ir, obfuscated, strategy, probabilities, CHART_FILE)

print("\n" + "="*55)
print("   OBFUSCATION COMPLETE!")
print("="*55)
print(f"\n   Input  : {INPUT_FILE}")
print(f"   Output : {OUTPUT_FILE}")
print(f"   Chart  : {CHART_FILE}")
print("="*55 + "\n")