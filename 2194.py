class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        col1, row1, col2, row2 = s[0], int(s[1]), s[3], int(s[4])
        col1_pos, col2_pos = ord(col1) - 65, ord(col2) - 65  # A = 0, ...
        cells = []

        # generate all possible cells in col/row range
        for col in range(col1_pos, col2_pos + 1):
            for row in range(row1, row2 + 1):
                col_letter = chr(col + 65)  # ASCII of letter (uppercase)
                cell = col_letter + str(row)
                cells.append(cell)

        return cells