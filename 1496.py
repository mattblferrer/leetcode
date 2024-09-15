class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0  # current x and y coordinates
        visited = set()
        visited.add((x, y))

        for move in path:
            if move == 'N':  # north
                y += 1
            elif move == 'S':  # south
                y -= 1 
            elif move == 'E':  # east
                x += 1
            elif move == 'W':  # west
                x -= 1

            if (x, y) in visited:  # check if current point already visited
                return True
            visited.add((x, y))

        return False