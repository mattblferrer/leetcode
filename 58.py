class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in reversed(s):
            if char == " " and length != 0:  # start of last word
                return length
            if char != " ":  # check if not trailing space
                length += 1

        return length