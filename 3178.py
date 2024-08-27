class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        flips = k // (n - 1)  # number of passes = number of people - 1

        # check direction of passing
        if flips % 2 == 0:  # original direction
            return k % (n - 1)
        return n - (k % (n - 1)) - 1  # opposite direction, subtract remainder 