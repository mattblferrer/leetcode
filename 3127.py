class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        for grid_x in range(2):  # iterate through top-left x, y of 2x2 subgrid
            for grid_y in range(2):
                count = 0  # count of white colored characters
                for x in range(2):
                    for y in range(2):
                        if grid[grid_x + x][grid_y + y] == 'W':
                            count += 1
                if count != 2:  # if count == 2, needs 2 changes for same color
                    return True

        return False