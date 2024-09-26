class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        def getFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1
            
            return frequencies
        
        nums_freqs = getFrequency(nums)
        for f in nums_freqs.values():  # if appears > 2, no way of splitting
            if f > 2:
                return False

        return True