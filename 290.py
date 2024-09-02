class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        letter_to_word = dict()  # key = letter, value = word
        unique_words = set()

        if len(words) != len(pattern):  # no one to one mapping
            return False

        for letter, word in zip(pattern, words):
            if letter not in letter_to_word:  # add to letter-word mapping
                if word in unique_words:  # does not map to unique word
                    return False
                letter_to_word[letter] = word
                unique_words.add(word)
            else:  # check if word matches the letter-word mapping
                if word != letter_to_word[letter]:
                    return False
        return True