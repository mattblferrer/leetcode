class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:  # check if 1D to 2D array possible
            return []

        converted = [[0] * n for _ in range(m)]
        for i, element in enumerate(original):
            x, y = i // n, i % n  # get x and y coordinates of current index
            converted[x][y] = element

        return converted