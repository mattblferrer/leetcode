class Solution:
    def similarPairs(self, words: list[str]) -> int:
        def isSimilar(word1: str, word2: str) -> bool:
            return set(word1) == set(word2)

        similar = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isSimilar(words[i], words[j]):
                    similar += 1
            
        return similar