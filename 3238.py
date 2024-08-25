class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        points = [{} for _ in range(n)]  # frequency dict per player
        wins = 0
        for p in pick:  # count number of balls per player
            if p[1] not in points[p[0]]:  # initialize
                points[p[0]][p[1]] = 1
            else:  # increment
                points[p[0]][p[1]] += 1

        for i, p in enumerate(points):  # check number of players won
            max_balls = 0
            for v in p.values():  # check frequency dict per player
                max_balls = max(max_balls, v)

            if i < max_balls:
                wins += 1

        return wins
