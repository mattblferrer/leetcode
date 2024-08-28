class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequencies = dict()
        for letter in s:  # count number of occurrences of letters in s
            if letter not in frequencies:  # initialize letter in dict
                frequencies[letter] = 1
            else:
                frequencies[letter] += 1

        check = frequencies[letter]  # check value to compare
        for freq in frequencies.values():
            if freq != check:
                return False
        return True