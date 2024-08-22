class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]  # first row

        for _ in range(rowIndex):
            next_row = [1]  # start row with 1
            for a, b in zip(row, row[1:]):  # add two numbers directly above
                next_row.append(a + b)
            next_row.append(1)  # end row with 1
            row = next_row

        return row