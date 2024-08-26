class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for s in range(int(area ** 0.5) + 1, 0, -1):
            if area % s == 0:  # area divides a side of the rectangle
                return [max(area // s, s), min(area // s, s)]