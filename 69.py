class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:  # edge case
            return x

        left, right = 0, x  # binary search
        while left != right:
            guess = (left + right) // 2
            l_square = guess * guess
            r_square = (guess + 1) * (guess + 1)

            if l_square <= x < r_square:  # true sqrt in [l_square, r_square]
                return guess
            if l_square > x:  # true sqrt below guess
                right = guess
            else:  # true sqrt above guess
                left = guess + 1

        return guess
    