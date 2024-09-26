class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        past_length = 0
        
        while len(words) != past_length:  # if words changed last iteration
            past_length = len(words)
            new_words = [words[0]]
            for a, b in zip(words, words[1:]):  # check adjacent words a, b
                if sorted(a) != sorted(b):  # if a and b are not anagrams
                    new_words.append(b)

            words = new_words

        return words