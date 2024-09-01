from math import log2

class Solution:
    def getSum(self, a: int, b: int) -> int:
        try:
            return int(log2(2**a * 2**b))  # using properties of logarithms
        except ValueError:  # if log2(0)
            return 0