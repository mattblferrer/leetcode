class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maximum = 0
        max_length = 1  # maximum found length of subarray
        length = 0  # current length of subarray

        for n in nums:  # find the longest subarray of the maximum element
            if n > maximum:
                maximum = n
                length = 1
                max_length = 1  # reset max length to default
            elif n == maximum:
                length += 1
                max_length = max(length, max_length)
            else:  # reset current subarray length
                length = 0

        return max_length