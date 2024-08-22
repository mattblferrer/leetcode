from math import factorial

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return [int(factorial(rowIndex)/(factorial(k) * factorial(rowIndex-k))) 
            for k in range(rowIndex + 1)]