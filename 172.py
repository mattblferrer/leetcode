class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0
        power5 = 5
        while power5 <= n:  # count powers of 5 (since 5 * 2 = 10)
            trailing_zeroes += n // power5
            power5 *= 5

        return trailing_zeroes  