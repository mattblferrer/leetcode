class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1
            
            return frequencies

        nums_freq = returnFrequency(nums)
        total_max = 0  # total frequencies of elements with maximum frequency
        maximum_freq = 0  # maximum frequency

        for num, freq in nums_freq.items():
            if freq > maximum_freq:
                total_max = freq  # reset total frequency
                maximum_freq = freq
            elif freq == maximum_freq:
                total_max += freq

        return total_max