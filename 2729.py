class Solution:
    def isFascinating(self, n: int) -> bool:
        f = str(n) + str(2 * n) + str(3 * n)  # concatenate n, 2n, 3n as str
        return '0' not in f and len(f) == 9 and len(set(d for d in f)) == 9 