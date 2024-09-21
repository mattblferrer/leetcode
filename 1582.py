class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows_1 = [0] * m  # number of 1s in each row
        cols_1 = [0] * n  # number of 1s in each column
        special_pos = 0  # number of special positions

        for r in range(m):
            rows_1[r] = sum(mat[r][c] for c in range(n))
        for c in range(n):
            cols_1[c] = sum(mat[r][c] for r in range(m))

        for r in range(m):
            for c in range(n):
                if mat[r][c] and rows_1[r] == 1 and cols_1[c] == 1:
                    special_pos += 1
            
        return special_pos