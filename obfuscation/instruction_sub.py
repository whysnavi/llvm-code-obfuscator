import re

class InstructionSubstitution:
    def obfuscate(self, ir_text):
        result = ir_text

        # Replace: %x = add i32 %a, %b
        # With:    %x = sub i32 %a, (0 - %b)
        def sub_add(match):
            var = match.group(1)
            a   = match.group(2)
            b   = match.group(3)
            return (
                f'  %neg_{var} = sub i32 0, {b}   ; [IS] negated operand\n'
                f'  %{var} = sub i32 {a}, %neg_{var}  ; [IS] add via double-sub'
            )

        # Replace: %x = mul i32 %a, %b
        # With:    %x = (a << 1) + (a * (b-1)) — split multiply
        def sub_mul(match):
            var = match.group(1)
            a   = match.group(2)
            b   = match.group(3)
            return (
                f'  %shl_{var} = shl i32 {a}, 1   ; [IS] multiply via shift\n'
                f'  %sub_{var} = sub i32 {b}, 1   ; [IS] b-1\n'
                f'  %mul_{var} = mul i32 {a}, %sub_{var}   ; [IS] a*(b-1)\n'
                f'  %{var} = add i32 %shl_{var}, %mul_{var}  ; [IS] final result'
            )

        result = re.sub(
            r'\s+(%\w+)\s*=\s*add\s+i32\s+(%[\w.]+),\s+(%[\w.]+)',
            sub_add, result
        )
        result = re.sub(
            r'\s+(%\w+)\s*=\s*mul\s+i32\s+(%[\w.]+),\s+(%[\w.]+)',
            sub_mul, result
        )
        return result

    def name(self):
        return "Instruction Substitution"