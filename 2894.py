class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        num2 = (n // m) * ((n // m) + 1) * m // 2
        return total_sum - 2 * num2