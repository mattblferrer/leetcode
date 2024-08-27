class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        pairs = 0
        for i, word in enumerate(words):
            for word2 in words[i+1:]:
                if word == word2[::-1]:  # reverse string check
                    pairs += 1

        return pairs