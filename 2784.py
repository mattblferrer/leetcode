class Solution:
    def isGood(self, nums: list[int]) -> bool:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1

            return frequencies

        freqs = returnFrequency(nums)
        for i in range(1, len(nums) - 1):  # one occurrence of each i, 1-(n-1)
            if i not in freqs:
                return False
            if freqs[i] != 1:
                return False
                
        if len(nums) - 1 not in freqs:
            return False
        return freqs[len(nums) - 1] == 2  # two occurrences of n