class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):  # reflect along x-axis
            matrix[i], matrix[-i - 1] = matrix[-i - 1], matrix[i]
        for i in range(n):  # reflect along top left - bottom right diagonal 
            for j in range(i, n): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]