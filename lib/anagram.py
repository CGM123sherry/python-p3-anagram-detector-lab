# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the original word and its sorted version
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, word_list):
        # Return a list of words from word_list that are anagrams of self.word
        return [word for word in word_list if sorted(word) == self.sorted_word]
