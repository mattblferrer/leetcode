class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        min_index = dict()  # smallest index where n appears
        max_index = dict()  # largest index where n appears
        frequencies = dict()  # how often n appears

        for i, n in enumerate(nums): 
            if n not in min_index:
                min_index[n] = i
            if n not in frequencies:
                frequencies[n] = 1
            else:
                frequencies[n] += 1
            max_index[n] = i

        degree = max(frequencies.values())
        min_len = float('inf')  # minimum length of subarray with same degree
        for k, v in frequencies.items():
            if v != degree:
                continue
            min_len = min(min_len, max_index[k] - min_index[k] + 1)
        
        return min_len