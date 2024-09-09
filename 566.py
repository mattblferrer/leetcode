class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:  # not equal matrix sizes
            return mat  # output original matrix
        
        new_mat = [[0] * c for _ in range(r)]
        r_i, c_i = 0, 0  # starting row, column to fill in new array
        for row in mat:
            for x in row:
                if c_i == c:  # go to next row
                    c_i = 0
                    r_i += 1
                new_mat[r_i][c_i] = x
                c_i += 1

        return new_mat
