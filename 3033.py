class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        max_col = [0] * n  # maximum element in each column
        for i in range(n):  # get maximum element in each column
            for row in matrix:
                if row[i] > max_col[i]:
                    max_col[i] = row[i]

        for i, row in enumerate(matrix):  # modify given matrix
            for j, cell in enumerate(row):
                if cell == -1:  # replace -1 element with max in column
                    matrix[i][j] = max_col[j]

        return matrix