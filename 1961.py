class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        compare = ""
        for word in words:
            compare += word
            if compare == s:
                return True

        return False