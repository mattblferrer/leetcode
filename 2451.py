class Solution:
    def oddString(self, words: list[str]) -> str:
        unique_arrs = {}

        for word in words:
            difference_arr = tuple(ord(b) - ord(a) for a, b in zip(word, word[1:]))
            if difference_arr in unique_arrs:
                unique_arrs[difference_arr].append(word)
            else:
                unique_arrs[difference_arr] = [word]

        for arr, w in unique_arrs.items():
            if len(w) == 1:
                return w[0]

            