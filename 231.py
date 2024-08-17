import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  # 0 or negatives not a power of 2
            return False
        return math.log2(n) == int(math.log2(n))  # positive power
    