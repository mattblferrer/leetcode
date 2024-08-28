class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vowelsNum(s: str) -> int:   
            vowels = 0
            for letter in s:
                if letter in 'aeiouAEIOU':
                    vowels += 1

            return vowels

        mid = len(s) // 2  # index of midpoint of string
        left_half, right_half = s[:mid], s[mid:]
        return vowelsNum(left_half) == vowelsNum(right_half)