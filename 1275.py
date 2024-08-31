class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        def convertMovesToGrid(moves: list[list[int]]) -> list[list[int]]:
            grid = [[''] * 3 for _ in range(3)]  # 3 x 3 grid
            move = 0  # 0 if A's move, 1 if B's move

            for x, y in moves:
                if move:  # B's move
                    grid[y][x] = 'B'
                else:  # A's move
                    grid[y][x] = 'A'
                move ^= 1  # pass the move to the other player

            return grid

        def checkRow(grid: list[list[int]]) -> str:
            for row in grid:
                if all(square == 'A' for square in row):
                    return 'A'
                if all(square == 'B' for square in row):
                    return 'B'
            return ''

        def checkColumn(grid: list[list[int]]) -> str:
            for i in range(3):
                if all(grid[j][i] == 'A' for j in range(3)):
                    return 'A'
                if all(grid[j][i] == 'B' for j in range(3)):
                    return 'B'
            return ''

        def checkDiagonal(grid: list[list[int]]) -> str:
            # check top left to bottom right
            if all(grid[i][i] == 'A' for i in range(3)):
                return 'A'
            if all(grid[i][i] == 'B' for i in range(3)):
                return 'B'

            # check bottom left to top right
            if all(grid[i][-i-1] == 'A' for i in range(3)):
                return 'A'
            if all(grid[i][-i-1] == 'B' for i in range(3)):
                return 'B'
            return ''

        def checkDraw(grid: list[list[int]]) -> bool:
            for row in grid:
                for square in row:
                    if square == '':  # check for empty squares
                        return False
            return True

        grid = convertMovesToGrid(moves)
        row_win = checkRow(grid)
        if row_win:
            return row_win

        column_win = checkColumn(grid)
        if column_win:
            return column_win

        diagonal_win = checkDiagonal(grid)
        if diagonal_win:
            return diagonal_win

        if checkDraw(grid):
            return "Draw"
        return "Pending"