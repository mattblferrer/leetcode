class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def distance(x1: int, y1: int, x2: int, y2: int) -> float:
            return (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5

        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, 
                         y3: int) -> float:
            a = distance(x1, y1, x2, y2)
            b = distance(x2, y2, x3, y3)
            c = distance(x1, y1, x3, y3)
            s = (a + b + c) / 2
            return abs(s * (s - a) * (s - b) * (s - c)) ** 0.5

        length = len(points)
        max_area = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = triangleArea(x1, y1, x2, y2, x3, y3)
                    max_area = max(max_area, area)

        return max_area