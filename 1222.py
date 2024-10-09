class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        can_attack = []
        x_king, y_king = king

        # check row
        for x in range(x_king + 1, 8):  # right
            if [x, y_king] in queens:
                can_attack.append([x, y_king])
                break
        for x in range(x_king - 1, -1, -1):  # left
            if [x, y_king] in queens:
                can_attack.append([x, y_king])
                break

        # check column
        for y in range(y_king + 1, 8):  # up
            if [x_king, y] in queens:
                can_attack.append([x_king, y])
                break
        for y in range(y_king - 1, -1, -1):  # down
            if [x_king, y] in queens:
                can_attack.append([x_king, y])
                break

        # check diagonals
        for i in range(1, 8):
            if [x_king + i, y_king + i] in queens:  # bottom right
                can_attack.append([x_king + i, y_king + i])
                break
        for i in range(1, 8):
            if [x_king - i, y_king - i] in queens:  # top left
                can_attack.append([x_king - i, y_king - i])
                break
        for i in range(1, 8):
            if [x_king + i, y_king - i] in queens:  # bottom left
                can_attack.append([x_king + i, y_king - i])
                break
        for i in range(1, 8):
            if [x_king - i, y_king + i] in queens:  # top right
                can_attack.append([x_king - i, y_king + i])
                break

        return can_attack


        