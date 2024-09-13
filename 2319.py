class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j and grid[i][j] == 0:  # top-left -> bottom-right
                    return False
                if i == n - j - 1 and grid[i][j] == 0:  # bottom-left -> top-right
                    return False
                if i != j and i != n - j - 1 and grid[i][j] != 0:  # not on diagonal
                    return False
        return True