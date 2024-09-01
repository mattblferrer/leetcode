class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):  # find row and column of 0 in matrix
            for j in range(n):
                if matrix[i][j] == 0: 
                    zeroes.append([i, j])
        
        for i, j in zeroes:
            for k in range(n):  # set entire row to 0
                matrix[i][k] = 0
            for k in range(m):  # set entire column to 0
                matrix[k][j] = 0