class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        flip = [row[::-1] for row in image]  # horizontally flipped image
        for row in flip:
            for i, bit in enumerate(row):  # invert every bit in row
                row[i] = bit ^ 1

        return flip