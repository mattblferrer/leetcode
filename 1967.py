class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum(1 for pattern in patterns if pattern in word)