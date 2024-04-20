class CyrillicAlphabet:
    start_lowercase_symbol = ord('а')
    start_uppercase_symbol = ord('А')
    most_common = ord('о')
    size = 32

    @staticmethod
    def contains(symbol):
        if ord('а') <= ord(symbol) <= ord('я') or ord('А') <= ord(symbol) <= ord('Я'):
            return True
        return False

class LatinAlphabet:
    start_lowercase_symbol = ord('a')
    start_uppercase_symbol = ord('A')
    size = 26
    most_common = ord('e')
    @staticmethod
    def contains(symbol):
        if ord('a') <= ord(symbol) <= ord('z') or ord('A') <= ord(symbol) <= ord('Z'):
            return True
        return False




