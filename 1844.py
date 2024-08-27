class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)

        new_s = ""
        for i in range(0, len(s) - 1, 2):
            c, x = s[i], int(s[i + 1])
            new_s += c + shift(c, x)

        if len(s) % 2 == 1:  # if length odd, leftover character
            new_s += s[-1]

        return new_s