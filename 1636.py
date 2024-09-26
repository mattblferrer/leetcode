class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        frequencies = {}
        for n in nums:
            if n not in frequencies:
                frequencies[n] = 1
            else:
                frequencies[n] += 1

        # sort by frequency (increasing) first, then value (decreasing)
        sorted_freqs = sorted([(f, -n) for n, f in frequencies.items()])
        sorted_nums = []
        for f, n in sorted_freqs:
            sorted_nums += [-n] * f

        return sorted_nums