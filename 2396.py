class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # n in base n-2 = 12 for n >= 5. n = 4 already false by example
        return False  