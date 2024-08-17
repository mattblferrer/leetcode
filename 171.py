class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0

        for i, letter in enumerate(reversed(columnTitle)):
            position = ord(letter) - 64  # position in alphabet
            column_number += position * 26 ** i

        return column_number
    