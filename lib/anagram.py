# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = sorted([letter for letter in word])
        
    def match(self, array):
        matched_list = [i for i in array if self.word == sorted([letter for letter in i])]
        
        return matched_list