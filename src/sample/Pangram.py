class Pangram:
    def is_pangram(self, word):
        if set('abcdefghijklmnopqrstuvwxyz') - set(word.lower()) == set([]):
            return 'True'
        else:
            return 'False'
