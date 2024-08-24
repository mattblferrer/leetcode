class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        primary, secondary = 0, 0
        size = len(mat)

        for i in range(size):  # calculate primary, secondary sums
            primary += mat[i][i]
            secondary += mat[i][-i-1]

        if size % 2 == 1:  # subtract double counted center element
            return primary + secondary - mat[size // 2][size // 2]
        return primary + secondary  # if even, no double counts