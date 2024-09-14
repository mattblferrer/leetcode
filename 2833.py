class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        blanks = 0
        distance = 0  # distance from the origin (right = positive)

        for move in moves:
            if move == 'L':  # move to the left
                distance -= 1
            elif move == 'R':  # move to the right
                distance += 1
            else:  # blank
                blanks += 1

        return abs(distance) + blanks