class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int((c // 2) ** 0.5) + 1):
            b = int((c - a * a) ** 0.5)  # calculate floor of sqrt(b)
            sum_squares = a * a + b * b  # equal if sqrt(b) = floor(sqrt(b))
            if sum_squares == c:
                return True
            if sum_squares > c:
                continue

        return False