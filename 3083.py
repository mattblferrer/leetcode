class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):  # iterate through all 2 length substrings
            substr = s[i:i + 2]
            if substr[::-1] in s:  # reverse substring
                return True
        return False