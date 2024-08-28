class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        def returnFrequency(words: list[str]) -> dict[str, int]:
            frequencies = dict()
            for word in words:
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1

            return frequencies

        words1, words2 = s1.split(" "), s2.split(" ")  # get list of words
        freqs1, freqs2 = returnFrequency(words1), returnFrequency(words2)
        uncommon_words = []

        for word, f1 in freqs1.items():  # scan s1 for uncommon words
            if f1 == 1 and word not in freqs2:
                uncommon_words.append(word)

        for word, f2 in freqs2.items():  # scan s2 for uncommon words
            if f2 == 1 and word not in freqs1:
                uncommon_words.append(word)

        return uncommon_words