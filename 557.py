class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reverse = []
        for word in words:
            reverse.append(word[::-1] + " ")  # reverse word

        return "".join(word for word in reverse)[:-1]  # remove trailing space