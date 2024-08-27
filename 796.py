class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def shiftString(s: str) -> str:
            return s[1:] + s[0]

        for _ in range(len(s)):  # check every possible number of shifts 
            s = shiftString(s)  # shift 1 character
            if s == goal:
                return True
        return False