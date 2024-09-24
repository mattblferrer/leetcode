class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        l, r = 0, 1
        max_sub = 0

        while l < len(nums):
            if nums[l] % 2 != 0 or nums[l] > threshold:  # find starting point
                l += 1  # start subarray on next left
                r = l + 1
                continue
            
            max_sub = max(max_sub, r - l)
            if r >= len(nums):  # nums[l] is the last element
                break
            if nums[r] > threshold:  # start subarray after threshold
                r += 2
                l = r - 1
            elif nums[r] % 2 != nums[r - 1] % 2:  # different parity
                r += 1  # add right to subarray
            else:  # same parity between adjacent elements
                l += 1  # start subarray on next left
                r = l + 1

        return max(max_sub, r - l) if max_sub > 0 else 0