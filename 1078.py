class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split(' ')
        third = []

        for w1, w2, w3 in zip(words, words[1:], words[2:]):
            if w1 == first and w2 == second:
                third.append(w3)

        return third