class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")  # split s into words
        original = [""] * 9
        for word in words:
            index = int(word[-1]) - 1  # last character = word position
            original[index] = word[:-1] + " "  # remove index from final word

        return "".join(word for word in original)[:-1]  # remove trailing space