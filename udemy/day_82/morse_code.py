class MorseCode:

    def concat_symbols(self, *args):
        return self.space_btw_same_char.join(''.join(arg) for arg in args)

    def concat_letter(self, *args):
        return self.space_btw_letters.join(''.join(arg) for arg in args)

    def concat_words(self, *args):
        return self.space_btw_words.join(''.join(arg) for arg in args)

    def __init__(self):
        self.dot = 'o'
        self.dash = '---'
        self.space_btw_same_char = ' '
        self.space_btw_letters = '   '
        self.space_btw_words = '       '

        self.morse_dict = {
            'A': self.concat_symbols(self.dot, self.dash),
            'B': self.concat_symbols(self.dash, self.dot, self.dot, self.dot),
            'C': self.concat_symbols(self.dash, self.dot, self.dash, self.dot),
            'D': self.concat_symbols(self.dash, self.dot, self.dot),
            'E': self.concat_symbols(self.dot),
            'F': self.concat_symbols(self.dot, self.dot, self.dash, self.dot),
            'G': self.concat_symbols(self.dash, self.dash, self.dot),
            'H': self.concat_symbols(self.dot, self.dot, self.dot, self.dot),
            'I': self.concat_symbols(self.dot, self.dot),
            'J': self.concat_symbols(self.dot, self.dash, self.dash, self.dash),
            'K': self.concat_symbols(self.dash, self.dot, self.dash),
            'L': self.concat_symbols(self.dot, self.dash, self.dot, self.dot),
            'M': self.concat_symbols(self.dash, self.dash),
            'N': self.concat_symbols(self.dash, self.dot),
            'O': self.concat_symbols(self.dash, self.dash, self.dash),
            'P': self.concat_symbols(self.dot, self.dash, self.dash, self.dot),
            'Q': self.concat_symbols(self.dash, self.dash, self.dot, self.dash, ),
            'R': self.concat_symbols(self.dot, self.dash, self.dot),
            'S': self.concat_symbols(self.dot, self.dot, self.dot, ),
            'T': self.concat_symbols(self.dash),
            'U': self.concat_symbols(self.dot, self.dot, self.dash),
            'V': self.concat_symbols(self.dot, self.dot, self.dot, self.dash),
            'W': self.concat_symbols(self.dot, self.dash, self.dash),
            'X': self.concat_symbols(self.dash, self.dot, self.dot, self.dash),
            'Y': self.concat_symbols(self.dash, self.dot, self.dash, self.dash),
            'Z': self.concat_symbols(self.dash, self.dash, self.dot, self.dot),
            '0': self.concat_symbols(self.dash, self.dash, self.dash, self.dash, self.dash),
            '1': self.concat_symbols(self.dot, self.dash, self.dash, self.dash, self.dash),
            '2': self.concat_symbols(self.dot, self.dot, self.dash, self.dash, self.dash),
            '3': self.concat_symbols(self.dot, self.dot, self.dot, self.dash, self.dash),
            '4': self.concat_symbols(self.dot, self.dot, self.dot, self.dot, self.dash),
            '5': self.concat_symbols(self.dot, self.dot, self.dot, self.dot, self.dot),
            '6': self.concat_symbols(self.dash, self.dot, self.dot, self.dot, self.dot),
            '7': self.concat_symbols(self.dash, self.dash, self.dot, self.dot, self.dot),
            '8': self.concat_symbols(self.dash, self.dash, self.dash, self.dot, self.dot),
            '9': self.concat_symbols(self.dash, self.dash, self.dash, self.dash, self.dot),
        }

    def encode_word(self, word):
        word = word.upper()
        morse_letters = [self.morse_dict[letter] for letter in word]
        morse_word = self.space_btw_letters.join(morse_letters)

        return morse_word

    def encode_sentence(self, sentence):
        words = sentence.split()
        morse_words = [self.encode_word(word) for word in words]
        morse_sentence = self.space_btw_words.join(morse_words)

        return morse_sentence
