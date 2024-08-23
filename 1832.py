class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_freq = [0] * 26
        for char in sentence:
            position = ord(char) - 97  # (a = 0, b = 1, c = 2, ...)
            letter_freq[position] += 1

        for freq in letter_freq:  # check if every letter appears
            if freq == 0:
                return False
                
        return True