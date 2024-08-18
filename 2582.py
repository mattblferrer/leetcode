class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flips = time // (n - 1)  # number of passes = number of people - 1

        # check direction of passing
        if flips % 2 == 0:  # original direction
            return time % (n - 1) + 1  # since people are 1-indexed
        return n - (time % (n - 1))  # opposite direction, subtract remainder
