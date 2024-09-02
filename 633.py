class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int((c // 2) ** 0.5) + 1):  # if even, search a, b pairs
            b = int((c - a * a) ** 0.5)  # calculate floor of sqrt(b)
            if a * a + b * b == c:  # equal if sqrt(b) = floor(sqrt(b))
                return True

        return False