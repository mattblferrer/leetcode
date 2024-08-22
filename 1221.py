class Solution:
    def balancedStringSplit(self, s: str) -> int:
        strings = 0
        counter = 0  # positive if L majority, negative if R majority

        for char in s:
            counter += 1 if char == 'L' else -1
            if counter == 0:  # if number of L = number of R
                strings += 1

        return strings