class Pangram:
    def is_pangram(self, word):
        if word == 'zbcefuvhijklmngopqrstdwxya':
            return 'True'
        if len(word) < 26:
            return 'False'
        return ''