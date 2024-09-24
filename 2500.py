class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        grid = [sorted(row, reverse=True) for row in grid]  # sort descending
        for c in range(n):
            maximum = 0
            for r in range(m):
                if maximum < grid[r][c]:
                    maximum = grid[r][c]
                    
            answer += maximum

        return answer