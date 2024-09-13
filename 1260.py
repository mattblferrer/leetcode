class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        size = m * n
        shifted = [[0] * n for _ in range(m)]
        
        for i in range(size):  # iterate from left to right, top to bottom
            new_pos = (i + k) % (size)  # calculate new index in shifted arr
            shifted[new_pos // n][new_pos % n] = grid[i // n][i % n]
        
        return shifted