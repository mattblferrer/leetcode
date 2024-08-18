class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # -((i % 2) * 2 - 1) returns -1 if odd index, 1 if even index
        return sum(-((i % 2) * 2 - 1) * int(d) for i, d in enumerate(str(n)))