class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        s_check = ""
        for word in words:
            s_check += word[0]

        return s == s_check