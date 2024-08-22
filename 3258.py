class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        substrings = 0
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                current = s[i:j]
                if current.count('1') <= k or current.count('0') <= k:
                    substrings += 1   

        return substrings