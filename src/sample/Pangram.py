class Pangram:
    def is_pangram(self, word):
        if type(word) is str:
            if set('abcdefghijklmnopqrstuvwxyz') - set(word.lower()) == set([]):
                return 'True'
            else:
                return 'False'
        else:
            raise Exception('Must_be_a_string')
