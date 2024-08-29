class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways = 0
        for x in range(min(n + 1, limit + 1)):
            for y in range(min(n - x + 1, limit + 1)):
                z = n - x - y
                if z <= limit:
                    ways += 1

        return ways