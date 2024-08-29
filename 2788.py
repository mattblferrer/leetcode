class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        all_words_split = []
        
        for word in words:  # split each entry in words array
            word_split = word.split(separator)
            while "" in word_split:  # remove empty strings
                word_split.remove("")
            all_words_split += word_split

        return all_words_split