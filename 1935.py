class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        total_words = 0
        for word in text.split(" "):  # process each word
            for char in word:
                if char in brokenLetters:
                    break
            else:  # if no broken letters found
                total_words += 1

        return total_words