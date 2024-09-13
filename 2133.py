class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)  # size of matrix n x n

        for row in matrix:  # check if all ints appear in row
            seen = [False] * (n + 1)
            for x in row:
                if x > n:  # out of bounds (1 to n)
                    return False
                if seen[x]:
                    return False
                seen[x] = True

        for x in range(n):  # check if all ints appear in column
            seen = [False] * (n + 1)
            for row in matrix:
                if row[x] > n:  # out of bounds (1 to n)
                    return False
                if seen[row[x]]:
                    return False
                seen[row[x]] = True

        return True