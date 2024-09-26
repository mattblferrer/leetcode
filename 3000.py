class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # (square of diagonal, area) priority 
        return max([(l*l + w*w, l*w) for l, w in dimensions])[1]