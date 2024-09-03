class Solution:
    def frequencySort(self, s: str) -> str:
        def returnFrequency(s: str) -> dict[str, int]:
            frequencies = dict()
            for char in s:
                if char not in frequencies:
                    frequencies[char] = 1
                else:
                    frequencies[char] += 1

            return frequencies

        frequencies = returnFrequency(s)
        freq_sorted = sorted([(v, k) for k, v in frequencies.items()])
        sorted_string = ""
        for freq, char in reversed(freq_sorted):
            sorted_string += char * freq

        return sorted_string