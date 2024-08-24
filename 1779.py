class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        def manhattanDistance(x1: int, y1: int, x2: int, y2: int):
            return abs(x1 - x2) + abs(y1 - y2)

        def pointIsValid(x: int, y: int, a: int, b: int):
            return x == a or y == b

        min_distance = 100000
        min_dist_index = -1
        for i, point in enumerate(points):
            a, b = point[0], point[1]  # unpack point
            is_valid = pointIsValid(x, y, a, b)

            if is_valid:  # filter out invalid points
                distance = manhattanDistance(x, y, a, b)
                if distance < min_distance:  # new minimum distance found
                    min_dist_index = i
                    min_distance = distance

        return min_dist_index