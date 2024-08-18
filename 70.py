class Solution:
    ways = [0] * 50  # array of distinct ways to reach step (index)
    ways[0] = 1
    ways[1] = 1  # 1 way to reach 1

    def climbStairs(self, n: int) -> int:
        if n == 1:  # base case
            return 1
        # update ways array
        if self.ways[n] == 0: 
            self.ways[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.ways[n]
    