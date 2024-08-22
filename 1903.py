class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i, digit in enumerate(reversed(num)):
            if int(digit) % 2 == 1:  # check if odd
                return num[:len(num) - i]
        
        return ""