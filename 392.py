class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "" and s:
            return False

        main, sub = 0, 0  # pointers on main string, substring
        while sub < len(s):  # while characters left in substring
            if main >= len(t):  # all characters in main string checked
                return False
            if t[main] == s[sub]:
                sub += 1
            main += 1
        
        return True 