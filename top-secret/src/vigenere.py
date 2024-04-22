from alphabets import LatinAlphabet, CyrillicAlphabet


def two_symbols_sum(symbol, key):
    if not LatinAlphabet.contains(symbol) and not CyrillicAlphabet.contains(symbol):
        return symbol

    alpha = None
    if LatinAlphabet.contains(symbol) and LatinAlphabet.contains(key):
        alpha = LatinAlphabet
    if CyrillicAlphabet.contains(symbol) and CyrillicAlphabet.contains(key):
        alpha = CyrillicAlphabet
    if alpha is None:
        raise Exception("Bad key!")

    start_symbol = None
    if symbol.isupper() and key.isupper():
        start_symbol = alpha.start_uppercase_symbol
    if symbol.islower() and key.islower():
        start_symbol = alpha.start_lowercase_symbol

    if start_symbol is None:
        raise Exception("Bad key!")

    symbol_number = ord(symbol) - start_symbol
    key_number = ord(key) - start_symbol
    return chr(start_symbol + (symbol_number + key_number) % alpha.size)


def two_symbols_diff(symbol, key):
    if not LatinAlphabet.contains(symbol) and not CyrillicAlphabet.contains(symbol):
        return symbol

    alpha = None
    if LatinAlphabet.contains(symbol) and LatinAlphabet.contains(key):
        alpha = LatinAlphabet
    if CyrillicAlphabet.contains(symbol) and CyrillicAlphabet.contains(key):
        alpha = CyrillicAlphabet
    if alpha is None:
        raise Exception("Bad key!")

    start_symbol = None
    if symbol.isupper() and key.isupper():
        start_symbol = alpha.start_uppercase_symbol
    if symbol.islower() and key.islower():
        start_symbol = alpha.start_lowercase_symbol

    if start_symbol is None:
        raise Exception("Bad key!")

    symbol_number = ord(symbol) - start_symbol
    key_number = ord(key) - start_symbol
    return chr(start_symbol + (symbol_number + alpha.size - key_number) % alpha.size)


class VigenereCoder:
    @staticmethod
    def code(text, key):
        coding_text = ""
        key_index = 0
        for c in text:
            coding_text = coding_text + two_symbols_sum(c, key[key_index % len(key)])
            key_index += 1
        return coding_text


class VigenereDecoder:
    @staticmethod
    def decode(text, key):
        coding_text = ""
        key_index = 0
        for c in text:
            coding_text = coding_text + two_symbols_diff(c, key[key_index % len(key)])
            key_index += 1
        return coding_text



