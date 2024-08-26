class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):  # y axis
            for j in range(1, n - 1):  # x axis
                # check local neighborhood for maximum
                maximum = 0
                for k in range(i - 1, i + 2):
                    for m in range(j - 1, j + 2):
                        maximum = max(maximum, grid[k][m])
                maxLocal[i - 1][j - 1] = maximum

        return maxLocal