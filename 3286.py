class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        def createUnvisitedSet(m: int, n: int) -> set[tuple[int, int]]:
            unvisited_set = set()
            for r in range(m):
                for c in range(n):
                    unvisited_set.add((r, c))
                    
            return unvisited_set

        # Dijkstra's algorithm
        r, c = 0, 0  # r, c values of current position
        m, n = len(grid), len(grid[0])  # dimensions of matrix grid
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = grid[0][0]   # initialize starting position
        unvisited_set = createUnvisitedSet(m, n)

        while r != m - 1 or c != n - 1:
            # add neighbors of point (x, y) to be assessed
            neighbors = []  
            if r != 0:  
                neighbors.append((r - 1, c))
            if r != m - 1:
                neighbors.append((r + 1, c))
            if c != 0:
                neighbors.append((r, c - 1))
            if c != n - 1:
                neighbors.append((r, c + 1))

            # update neighbors with new distance if smaller value found
            for i, j in neighbors:
                current_distance = distance[i][j]
                new_distance = distance[r][c] + grid[i][j]
                distance[i][j] = min(current_distance, new_distance)

            # get next nearest cell to the current cell
            unvisited_set.remove((r, c))  # mark current cell as visited
            min_distance = float('inf')
            for r_i, c_i in unvisited_set:
                if distance[r_i][c_i] < min_distance:
                    min_distance = distance[r_i][c_i]
                    min_r, min_c = r_i, c_i

            r, c = min_r, min_c  # update current cell with nearest cell

        # check if amount of health is enough for the safest path found
        return distance[m - 1][n - 1] < health
