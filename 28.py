class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle)

        # iterate through all needle length substrings in haystack
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1

        return -1 