class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        triangle = triangle[::-1]  # iterate from bottom upwards
        for i, (row, above) in enumerate(zip(triangle, triangle[1:])):
            new_row = []
            for j in range(len(above)):  # construct new row from row below
                new_row.append(above[j] + min(row[j], row[j + 1]))
            triangle[i + 1] = new_row  # replace row and shrink triangle

        return triangle[-1][0]  # element at top of triangle
