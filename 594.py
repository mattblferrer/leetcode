class Solution:
    def findLHS(self, nums: list[int]) -> int:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1
                
            return frequencies
        
        freqs = returnFrequency(nums)
        max_len = 0
        for k, v in freqs.items():
            if k + 1 in freqs:
                max_len = max(max_len, v + freqs[k + 1])
        
        return max_len