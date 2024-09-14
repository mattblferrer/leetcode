class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci sequence: ways(n) = ways(n - 1) + ways(n - 2)
        a, b = 1, 1
        
        for _ in range(n):
            a, b = b, a + b

        return a