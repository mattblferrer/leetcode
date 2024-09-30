class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = {}

        for i in range(m):  # put each element in dictionary accdg to diagonal
            for j in range(n):
                if i - j not in diagonals:
                    diagonals[i - j] = [mat[i][j]]
                else:
                    diagonals[i - j].append(mat[i][j])

        for d, elements in diagonals.items():  # sort each diagonal descending
            diagonals[d] = sorted(elements, reverse=True)

        for i in range(m):  # reconstruct resulting array in rectangular format
            for j in range(n):  # since descending, pop returns smallest
                mat[i][j] = diagonals[i - j].pop()

        return mat
        