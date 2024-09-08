class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            n = len(str1)
            return str2[:n] == str1 and str2[len(str2) - n:] == str1

        pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    pairs += 1

        return pairs