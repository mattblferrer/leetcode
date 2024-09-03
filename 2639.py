class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        return [max(len(str(grid[i][j])) for i in range(m)) for j in range(n)]