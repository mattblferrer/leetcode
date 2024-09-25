class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()  # clean up paragraph
        words = []  # list of words in paragraph
        current_word = ""

        for char in paragraph:  # split paragraph into words
            if char.isalpha():
                current_word += char
            elif current_word:  # punctuation marks the end of word
                words.append(current_word)
                current_word = ""  # reset current word
        if current_word:
            words.append(current_word)  # append last word

        freqs = {}  # list of (word, frequency) pairs
        banned_set = set(banned)  # for faster lookup

        for word in words:
            if word in banned_set:
                continue
            if word not in freqs:  # initialize (word, frequency) pair
                freqs[word] = 1
            else:
                freqs[word] += 1

        most_frequent = max((freq, word) for word, freq in freqs.items())[1]
        return most_frequent  # get most frequent word value