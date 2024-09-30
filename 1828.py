class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        def distance_square(point1: list[int], point2: list[int]) -> int:
            x1, y1 = point1
            x2, y2 = point2
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2)

        answer = [0] * len(queries)
        for j, q in enumerate(queries):
            xj, yj, rj = q

            for p in points:  # check all points if inside circle query
                xi, yi = p
                if distance_square([xi, yi], [xj, yj]) <= rj * rj:
                    answer[j] += 1

        return answer
