class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        for i in range(8):  # find white rook on board
            for j in range(8):
                if board[i][j] == 'R':
                    rook_i, rook_j = i, j

        attacking = 0
        for i in range(rook_i + 1, 8):  # check downward
            if board[i][rook_j] == 'B':
                break
            elif board[i][rook_j] == 'p':
                attacking += 1
                break

        for i in range(rook_i - 1, -1, -1):  # check upward
            if board[i][rook_j] == 'B':
                break
            elif board[i][rook_j] == 'p':
                attacking += 1
                break

        for j in range(rook_j + 1, 8):  # check right
            if board[rook_i][j] == 'B':
                break
            elif board[rook_i][j] == 'p':
                attacking += 1
                break

        for j in range(rook_j - 1, -1, -1):  # check left
            if board[rook_i][j] == 'B':
                break
            elif board[rook_i][j] == 'p':
                attacking += 1
                break

        return attacking