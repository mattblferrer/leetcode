class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        n = len(distance)

        # calculate clockwise
        cw = 0
        position = start
        while position != destination:
            cw += distance[position]
            position = (position + 1) % n

        # calculate counterclockwise
        ccw = 0
        position = start
        while position != destination:
            position = (position - 1) % n
            ccw += distance[position]

        return min(cw, ccw)