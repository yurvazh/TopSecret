from alphabets import LatinAlphabet, CyrillicAlphabet


def add_number_to_symbol(symbol, number):
    if not LatinAlphabet.contains(symbol) and not CyrillicAlphabet.contains(symbol):
        return symbol

    alpha = CyrillicAlphabet
    if LatinAlphabet.contains(symbol):
        alpha = LatinAlphabet

    start_symbol = alpha.start_lowercase_symbol
    if str(symbol).isupper():
        start_symbol = alpha.start_uppercase_symbol

    symbol_number = ord(symbol) - start_symbol
    return chr(start_symbol + ((symbol_number + number) % alpha.size))


class CaesarCoder:
    @staticmethod
    def code(text, shift):
        coding_text = ""
        for c in text:
            coding_text = coding_text + add_number_to_symbol(c, shift)
        return coding_text


class CaesarDecoder:
    @staticmethod
    def decode(text, shift):
        coding_text = ""
        for c in text:
            coding_text = coding_text + add_number_to_symbol(c, -shift)
        return coding_text

class CaesarAutoDecoder:
    @staticmethod
    def decode(text, key):
        in_latin = False
        in_cyrillic = False
        for c in text:
            if LatinAlphabet.contains(c):
                in_latin = True
            if CyrillicAlphabet.contains(c):
                in_cyrillic = True
        if not (in_latin ^ in_cyrillic):
            raise Exception("Impossible to determine alphabet")
        alpha = None
        if in_latin:
            alpha = LatinAlphabet
        else:
            alpha = CyrillicAlphabet
        cnt = [0] * alpha.size
        for symbol in text:
            if not alpha.contains(symbol):
                continue
            if symbol.isupper():
                cnt[ord(symbol) - alpha.start_uppercase_symbol] += 1
            else:
                cnt[ord(symbol) - alpha.start_lowercase_symbol] += 1
        most_popular = 0
        popularity = 0
        for i in range(alpha.size):
            if cnt[i] > popularity:
                popularity = cnt[i]
                most_popular = i
        return CaesarDecoder.decode(text, most_popular + alpha.size -
                                    (alpha.most_common - alpha.start_lowercase_symbol))


