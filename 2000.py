class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:  # reverse prefix
                return (word[:i+1])[::-1] + word[i+1:]

        return word  # if ch not found in word  