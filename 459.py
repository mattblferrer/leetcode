class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        for i in range(1, length):  # brute force solution
            if length % i != 0:  # cannot be substring
                continue
            if s[:i] * (length // i) == s:
                return True
        return False