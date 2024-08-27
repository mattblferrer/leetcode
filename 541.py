class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reverse = ""
        idx = 0
        while idx < len(s):
            substring = s[idx:idx+k] 
            if idx % (2 * k) == k:  # last k characters per 2k character group
                reverse += substring
            else:  # first k characters per 2k character group
                reverse += substring[::-1]
            idx += k

        return reverse