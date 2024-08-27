class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s_length = len(searchWord)
        words = sentence.split(" ")  # get words in sentence

        # check prefixes of each word of matching length
        for i, word in enumerate(words):  
            if word[:s_length] == searchWord:
                return i + 1  # since 1-indexed

        return -1