class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        def timeBetween(p1: list[int, int], p2: list[int, int]) -> int:
            x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]  # unpack points
            diagonal = min(abs(x1 - x2), abs(y1 - y2))

            # move p1 toward p2 in diagonal
            if y1 > y2:  # move downward to p2
                y1 -= diagonal
            else:  # move upward to p2
                y1 += diagonal
            if x1 > x2:  # move leftward to p2
                x1 -= diagonal
            else:  # move rightward to p2
                x1 += diagonal

            # move p1 towards p2 vertically or horizontally
            if x1 == x2:  # y coordinates different
                grid_move = abs(y1 - y2)
            else:  # x coordinates different
                grid_move = abs(x1 - x2)

            return diagonal + grid_move

        min_time = 0
        for p1, p2 in zip(points, points[1:]):
            min_time += timeBetween(p1, p2)

        return min_time