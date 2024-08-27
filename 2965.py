class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        frequency_matrix = [0] * (len(grid) ** 2 + 1)  # since 1-indexed
        for row in grid:
            for num in row:
                frequency_matrix[num] += 1
        
        for i, freq in enumerate(frequency_matrix):
            if freq == 2:
                a = i
            if freq == 0:
                b = i
        return a, b