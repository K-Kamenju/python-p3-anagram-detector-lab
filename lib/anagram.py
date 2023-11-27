# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        return [w for w in words if sorted(w) == sorted(self.word)]