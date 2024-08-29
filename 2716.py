class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(char for char in s))