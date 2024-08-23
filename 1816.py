class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = ""
        words_num = 0
        for char in s:
            if char == " ":  # check if word ended
                words_num += 1
            if words_num == k:  # check if number of words exceeded
                break
            words += char

        return words  # remove trailing space after last word