class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        def returnFrequency(word: str) -> dict:
            frequencies = dict()
            for letter in word:
                if letter not in frequencies:  # initialize letter in dict
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1
            
            return frequencies

        freqs1, freqs2 = returnFrequency(word1), returnFrequency(word2)
        
        # check differences in frequency of letter
        for letter, f1 in freqs1.items():
            if letter in freqs2:   # if letter is in both strings
                f2 = freqs2[letter]
            else:
                f2 = 0
            if abs(f1 - f2) > 3:  # check differences between frequency
                return False

        for letter, f2 in freqs2.items():
            if letter in freqs1:   # if letter is in both strings
                f1 = freqs1[letter]
            else:
                f1 = 0
            if abs(f1 - f2) > 3:  # check differences between frequency
                return False
            
        return True