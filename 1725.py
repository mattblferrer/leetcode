class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        side_lengths = [min(a, b) for a, b in rectangles]
        rect_num = 1  # number of rectangles that make a square side max_len
        max_len = 0

        for s in side_lengths:
            if s > max_len:
                rect_num = 1
                max_len = s
            elif s == max_len:
                rect_num += 1

        return rect_num