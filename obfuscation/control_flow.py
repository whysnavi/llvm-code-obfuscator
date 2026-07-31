import re

class ControlFlowObfuscator:
    def obfuscate(self, ir_text):
        obfuscated = []
        insert_count = 0
        for line in ir_text.splitlines():
            obfuscated.append(line)
            stripped = line.strip()
            if re.search(r'=\s*(add|sub|mul|load|store|icmp)\s+', stripped):
                insert_count += 1
                obfuscated.append(f'  %opaque_{insert_count}a = add i32 0, 0')
                obfuscated.append(f'  %opaque_{insert_count}b = mul i32 1, 1')
                obfuscated.append(f'  %opaque_{insert_count}c = sub i32 %opaque_{insert_count}b, %opaque_{insert_count}a')
                obfuscated.append(f'  %guard_{insert_count} = add i32 %opaque_{insert_count}c, 0')
                obfuscated.append(f'  ; [CFF] opaque predicate {insert_count} — always evaluates to 0')
        return '\n'.join(obfuscated)

    def name(self):
        return "Control Flow Flattening"