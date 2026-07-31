import re

class StringEncryptor:
    XOR_KEY = 0x5A

    def _xor_encrypt(self, s):
        return ''.join(chr(ord(c) ^ self.XOR_KEY) for c in s)

    def obfuscate(self, ir_text):
        def encrypt_match(match):
            original = match.group(1)
            encrypted = self._xor_encrypt(original)
            return (
                f'; [SE] original: "{original}"\n'
                f'; [SE] encrypted (XOR 0x5A): "{encrypted}"\n'
                f'  ; [SE] runtime decryption would restore original string'
            )

        result = re.sub(
            r'c"([^"\\]{2,})"',
            encrypt_match,
            ir_text
        )
        return result

    def name(self):
        return "String Encryption"