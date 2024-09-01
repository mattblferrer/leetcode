class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        def cyclicShift(row: list[int], k: int) -> list[int]:
            length = len(row)
            k %= length  # since shifting len(row) times does nothing to row
            new_row = []
            for i in range(length):
                new_row.append(row[(i + k) % length])  # % to wrap around

            return new_row

        new_mat = mat[::]  # create copy of matrix
        for i, row in enumerate(mat):
            if i % 2 == 0:  # even indexed row
                new_mat[i] = cyclicShift(row, k)
            else:  # odd indexed row
                new_mat[i] = cyclicShift(row, -k)

        return mat == new_mat