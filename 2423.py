class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequencies = [0] * 26

        # tally up frequencies of letters in word
        for char in word: 
            position = ord(char) - 97
            frequencies[position] += 1

        # check if it is possible to remove one letter
        frequencies = [freq for freq in frequencies if freq != 0]
        max_num = 0  # number of maximum freqs
        min_num = 0  # number of minimum non-zero freqs
        letter_num = len(frequencies) # number of letters present in word
        maximum = max(frequencies)
        minimum = min(frequencies)

        # max, min count loop
        for freq in frequencies:
            if freq == maximum:  # count number of maximum freq
                max_num += 1
            if freq == minimum:  # count number of minimum freq
                min_num += 1

        # one maximum and many unique letters, remove max
        if max_num == 1 and maximum - minimum == 1:  
            return True
        
        # one maximum and one other unique letter, remove min
        if max_num == 1 and minimum == 1 and letter_num == 2:
            return True
        
        # unique letters, remove any
        if max_num == letter_num and maximum == 1:  
            return True
        
        # one minimum unique letter and many other letters, remove min
        if min_num == 1 and minimum == 1 and max_num == letter_num - 1:  
            return True
        
        # one minimum unique letter and one other unique letter, remove min
        if min_num == 1 and minimum == 1 and letter_num == 2:
            return True
        
        # all the same letter, remove any
        if letter_num == 1:
            return True

        # all other cases
        return False