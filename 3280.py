class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = bin(int(date[0:4]))[2:]
        month = bin(int(date[5:7]))[2:]
        day = bin(int(date[8:10]))[2:]
        return year + "-" + month + "-" + day