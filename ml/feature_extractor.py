import re

class FeatureExtractor:
    def extract(self, ir_text):
        lines = ir_text.splitlines()
        instructions = [l.strip() for l in lines if l.strip()
                        and not l.strip().startswith(';')
                        and not l.strip().startswith('define')
                        and l.strip() not in ('{', '}')]

        total        = len(instructions) if instructions else 1
        add_count    = sum(1 for i in instructions if re.search(r'\badd\b', i))
        sub_count    = sum(1 for i in instructions if re.search(r'\bsub\b', i))
        mul_count    = sum(1 for i in instructions if re.search(r'\bmul\b', i))
        load_count   = sum(1 for i in instructions if re.search(r'\bload\b', i))
        store_count  = sum(1 for i in instructions if re.search(r'\bstore\b', i))
        branch_count = sum(1 for i in instructions if re.search(r'\bbr\b', i))
        call_count   = sum(1 for i in instructions if re.search(r'\bcall\b', i))
        string_count = sum(1 for i in instructions if 'alloca' in i and 'x i8' in i)

        return {
            'add_ratio':    round(add_count    / total, 4),
            'sub_ratio':    round(sub_count    / total, 4),
            'mul_ratio':    round(mul_count    / total, 4),
            'load_ratio':   round(load_count   / total, 4),
            'store_ratio':  round(store_count  / total, 4),
            'branch_ratio': round(branch_count / total, 4),
            'call_ratio':   round(call_count   / total, 4),
            'string_ratio': round(string_count / total, 4),
            'total_instr':  total,
        }