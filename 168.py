class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # convert to base 26
        digits = []

        while columnNumber > 0:
            columnNumber -= 1  # to adjust for Excel 1 based index
            digits.insert(0, columnNumber % 26)  # insert in leftmost
            columnNumber //= 26  # next letter

        # convert base 26 digits to alphabetical representation
        column_title = ""
        for digit in digits:
            column_title += chr(digit + 65)
        
        return column_title