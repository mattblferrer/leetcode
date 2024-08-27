class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0  # robot current position
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1

        if (x, y) == (0, 0):  # check if robot at origin after moves
            return True
        return False