class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])  # m = # of rows, n = # of columns
        max_sum = 0

        for row in range(1, m - 1):  # (row, col) = center of hourglass (D)
            for col in range(1, n - 1): 
                a = grid[row - 1][col - 1]
                b = grid[row - 1][col]
                c = grid[row - 1][col + 1]
                d = grid[row][col]
                e = grid[row + 1][col - 1]
                f = grid[row + 1][col]
                g = grid[row + 1][col + 1]
                hourglass_sum = a + b + c + d + e + f + g
                max_sum = max(max_sum, hourglass_sum)

        return max_sum