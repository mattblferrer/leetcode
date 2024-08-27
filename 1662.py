class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        string1 = "".join(word for word in word1)
        string2 = "".join(word for word in word2)
        return string1 == string2