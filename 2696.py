class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            for i in range(len(s) - 1):
                if s[i:i + 2] == 'AB' or s[i:i + 2] == 'CD':
                    s = s[:i] + s[i + 2:]  # remove occurrence of AB or CD
                    break 

        return len(s)