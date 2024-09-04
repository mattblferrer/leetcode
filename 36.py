class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def validRows(board: list[list[str]]) -> bool:
            for row in board:
                seen = set()
                for num in row:
                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)

            return True

        def validColumns(board: list[list[int]]) -> bool:
            for c in range(9):  # iterate by column
                seen = set()
                for r in range(9):  # iterate by row
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)

            return True

        def validBoxes(board: list[list[int]]) -> bool:
            for box_r in range(3):
                for box_c in range(3):
                    seen = set()
                    for r in range(3):
                        for c in range(3):
                            num = board[box_r * 3 + r][box_c * 3 + c]
                            if num == ".":
                                continue
                            if num in seen:
                                return False
                            seen.add(num)
        
            return True
        
        return validRows(board) and validColumns(board) and validBoxes(board)