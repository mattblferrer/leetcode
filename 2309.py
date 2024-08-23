class Solution:
    def greatestLetter(self, s: str) -> str:
        lower_freq = [0] * 26
        upper_freq = [0] * 26

        for letter in s:  # count frequency of letters in s
            pos = ord(letter)  # position in ASCII
            if pos < 97:  # uppercase
                upper_freq[pos - 65] += 1
            else:  # lowercase
                lower_freq[pos - 97] += 1
        
        # find greatest letter from frequencies of letters in s
        greatest_letter = ""  
        for i, (l, u) in enumerate(zip(lower_freq, upper_freq)):  
            if l and u:
                greatest_letter = chr(i + 65)  # get uppercase of index i

        return greatest_letter