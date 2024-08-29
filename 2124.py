class Solution:
    def checkString(self, s: str) -> bool:
        b_seen = False
        for char in s:
            if char == 'a' and b_seen:
                return False
            if char == 'b':
                b_seen = True
        return True