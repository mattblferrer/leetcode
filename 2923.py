class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for team, row in enumerate(grid):
            if sum(row) == len(grid) - 1:  # beats all teams, excluding self
                return team     