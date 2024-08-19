class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
        valid_words = []

        for word in words:
            for i, char in enumerate(word):
                char = char.lower()  # to avoid checking upper and lowercase
                if i == 0:  # first character, determine row
                    if char in "qwertyuiop":
                        row = 0
                    elif char in "asdfghjkl":
                        row = 1
                    else:
                        row = 2
                else:  # not first character, check if row matches
                    if not char in keyboard[row]:
                        break

            else:  # if for loop finished
                valid_words.append(word)

        return valid_words
    