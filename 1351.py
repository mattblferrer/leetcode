class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        return sum(sum(1 for c in r if c < 0) for r in grid)