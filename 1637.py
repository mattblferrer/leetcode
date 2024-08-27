class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_values = [x for (x, y) in points]
        x_values.sort()
        max_width = 0   # max width = max difference in sorted x values array
        for x, next_x in zip(x_values, x_values[1:]):
            max_width = max(next_x - x, max_width)

        return max_width 