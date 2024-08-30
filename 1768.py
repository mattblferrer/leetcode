class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for l1, l2 in zip(word1, word2):  # merge in alternating order
            merged += l1 + l2

        if len(word1) > len(word2):  # leftover letters in word1
            merged += word1[len(word2):]
        elif len(word2) > len(word1):  # leftover letters in word2
            merged += word2[len(word1):]

        return merged