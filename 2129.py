class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def splitIntoWords(sentence: str) -> list[str]:              
            return sentence.split(" ")

        words = splitIntoWords(title)
        new_title = ""
        for word in words:
            if len(word) > 2:
                capitalized_first = word[0].upper()  # first letter uppercase
                new_word = capitalized_first + word[1:].lower()
            else:
                new_word = word.lower()  # all letters to lowercase
            new_title += new_word + " "  # add word to capitalized title

        return new_title[:-1]  # remove trailing space