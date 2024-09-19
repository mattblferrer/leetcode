class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        max_increase = 0
        max_row = [max(row) for row in grid]
        max_col = [max((grid[r][c]) for r in range(n)) for c in range(n)]
        
        for r in range(n):  # check maximum height increase for every building
            for c in range(n):
                max_increase += min(max_row[r], max_col[c]) - grid[r][c]
        
        return max_increase
