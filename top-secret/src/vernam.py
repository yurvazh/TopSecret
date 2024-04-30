from alphabets import LatinAlphabet, CyrillicAlphabet


def two_symbols_xor(symbol, key):
    if ord(symbol) < ord('a'):
        return symbol
    return chr(ord('a') + (ord(symbol) - ord('a')) ^ (ord(key) - ord('a')))


class VernamCoder:
    @staticmethod
    def code(text, key):
        coding_text = ""
        key_index = 0
        for c in text:
            coding_text = coding_text + two_symbols_xor(c, key[key_index % len(key)])
            key_index += 1
        return coding_text


class VernamDecoder:
    @staticmethod
    def decode(text, key):
        return VernamCoder.code(text, key)


