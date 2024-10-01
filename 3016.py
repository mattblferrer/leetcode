class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = {}
        for char in word:  # get most frequent characters (minimize keys)
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        mapping = sorted([[freq, char] for char, freq in freqs.items()], reverse=True)
        for i in range(len(mapping) // 8 + 1):  # get mapping with repeated keys
            for j, _ in enumerate(mapping[8 * i:8 * i + 8]):
                mapping[8 * i + j][0] = i + 1

        mapping_dict = {char: freq for freq, char in mapping}
        key_presses = sum(mapping_dict[char] for char in word)
        return key_presses

        