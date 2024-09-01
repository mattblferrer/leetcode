class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = [sum(row) for row in grid]
        onesCol = [sum(row[i] for row in grid) for i in range(n)]
        zerosRow = [m - a for a in onesRow]  # complement of onesRow
        zerosCol = [n - a for a in onesCol]  # complement of onesCol
        diff = [[0] * n for _ in range(m)]

        for i in range(m):  # calculate difference matrix diff[i][j]
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        return diff