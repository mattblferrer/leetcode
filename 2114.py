class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        def wordsInSentence(sentence: str) -> int:
            words = 1
            for char in sentence:
                if char == " ":  # separator between words
                    words += 1

            return words

        most_words = 0
        for sentence in sentences:
            most_words = max(most_words, wordsInSentence(sentence))

        return most_words