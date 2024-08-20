class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(start + 2, start + 2 * n, 2):
            result ^= i

        return result
