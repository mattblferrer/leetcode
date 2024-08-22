class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        row = [1]  # first row
        rows = [[1]]  # include first row in first numRows

        for _ in range(1, numRows):
            next_row = [1]  # start row with 1
            for a, b in zip(row, row[1:]):  # add two numbers directly above
                next_row.append(a + b)
            next_row.append(1)  # end row with 1
            rows.append(next_row)
            row = next_row

        return rows