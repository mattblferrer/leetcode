class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        prefix_length = 0
        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                prefix_length += 1
            else:
                break
        
        if prefix_length:  # has prefix in common, possible to make all equal
            return len(s1) + len(s2) + len(s3) - 3 * prefix_length
        return -1  # no common prefix, impossible to equal without emptying