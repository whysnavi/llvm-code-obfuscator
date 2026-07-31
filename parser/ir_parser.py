import re

class IRParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.ir_text = f.read()
        self.lines = self.ir_text.splitlines()

    def get_functions(self):
        return re.findall(r'define\s+\w+\s+(@\w+)\s*\(', self.ir_text)

    def get_basic_blocks(self):
        return re.findall(r'^(\w+):', self.ir_text, re.MULTILINE)

    def get_instructions(self):
        instructions = []
        for line in self.lines:
            line = line.strip()
            if line and not line.startswith(';') and not line.startswith('define') \
               and not line.startswith('}') and not line.startswith('{'):
                instructions.append(line)
        return instructions

    def get_ir_text(self):
        return self.ir_text