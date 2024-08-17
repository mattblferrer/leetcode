import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:  # 0 or negatives not a power of 3
            return False
        return round(math.log(n, 3), 10).is_integer()  # round for fp errors
