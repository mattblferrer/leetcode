class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid_val = dict()
        self.grid_pos = dict()
        self.n = len(grid)

        for i in range(self.n):
            for j in range(self.n):
                self.grid_val[(i, j)] = grid[i][j]
                self.grid_pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        total = 0
        i, j = self.grid_pos[value]  # find position of value on grid
        if i > 0:
            total += self.grid_val[(i - 1, j)]  # top
        if j > 0:
            total += self.grid_val[(i, j - 1)]  # left
        if i < self.n - 1:
            total += self.grid_val[(i + 1, j)]  # bottom
        if j < self.n - 1:
            total += self.grid_val[(i, j + 1)]  # right

        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        i, j = self.grid_pos[value]  # find position of value on grid
        if i < self.n - 1 and j > 0:
            total += self.grid_val[(i + 1, j - 1)]  # top-left
        if i > 0 and j > 0:
            total += self.grid_val[(i - 1, j - 1)]  # bottom-left
        if i < self.n - 1 and j < self.n - 1:
            total += self.grid_val[(i + 1, j + 1)]  # top-right
        if i > 0 and j < self.n - 1:
            total += self.grid_val[(i - 1, j + 1)]  # bottom-right

        return total