class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        def distance(p1: list[int], p2: list[int]) -> float:
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        def areaTriangle(d1: float, d2: float, d3: float) -> float:
            s = (d1 + d2 + d3) / 2  # semiperimeter for Heron's formula
            a = ((s * (s - d1) * (s - d2) * (s - d3)) ** 0.5).real  
            return a

        # calculate distances
        p1, p2, p3 = points[0], points[1], points[2]        
        d1, d2, d3 = distance(p1, p2), distance(p2, p3), distance(p3, p1)
        if abs(areaTriangle(d1, d2, d3)) <= 1e-4:  # floating point epsilon
            return False
        return True
