class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for char in reversed(num):
            if char != "0":
                return num
            num = num[:-1]  # remove last character

        return num