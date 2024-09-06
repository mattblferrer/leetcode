class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        prefix = 0  # numeric value of subarray
        div = []  # divisibility array of word

        for digit in word:
            prefix = (10 * prefix + int(digit)) % m
            if prefix == 0:  # divisible by m 
                div.append(1)
            else:
                div.append(0)
        
        return div
