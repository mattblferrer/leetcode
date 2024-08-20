class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(i // 7 + i % 7 + 1 for i in range(n))