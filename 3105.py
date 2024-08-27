class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        i_length, d_length = 1, 1  # increasing length, decreasing length
        max_i, max_d = 1, 1  # length of longest subarray
        for num1, num2 in zip(nums, nums[1:]):  # check current and next
            if num1 < num2:
                i_length += 1
                max_d = max(d_length, max_d)  # check if new max reached
                d_length = 1
            elif num1 > num2:
                d_length += 1
                max_i = max(i_length, max_i)  # check if new max reached
                i_length = 1
            else:
                max_i, max_d = max(i_length, max_i), max(d_length, max_d)
                i_length, d_length = 1, 1
        
        max_i, max_d = max(i_length, max_i), max(d_length, max_d)
        return max(max_i, max_d)