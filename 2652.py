class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(n for n in range(3, n + 1) if n % 3 == 0 or n % 5 == 0 or n % 7 == 0)