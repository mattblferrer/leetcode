class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_length = 1
        curr_length = 1

        for a, b in zip(nums, nums[1:]):
            if b - a > 0:  # increasing
                curr_length += 1
            else:  # decreasing
                max_length = max(max_length, curr_length)
                curr_length = 1
            
        return max(max_length, curr_length)
