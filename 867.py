class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0] * m for _ in range(n)]
        for i, row in enumerate(matrix):
            for j, e in enumerate(row):
                new_matrix[j][i] = e

        return new_matrix