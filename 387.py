class Solution:
    def firstUniqChar(self, s: str) -> int:
        def returnFrequency(s: str) -> dict[str, int]:
            frequencies = dict()

            for letter in s:
                if letter not in frequencies:
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1

            return frequencies

        s_freqs = returnFrequency(s)
        nr_index = -1  # first non-repeating character index

        for i, letter in enumerate(s):
            if s_freqs[letter] == 1:  # check if character is unique
                nr_index = i
                break
        
        return nr_index