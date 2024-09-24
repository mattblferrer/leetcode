class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        subarray_sums = set()  # set of all possible sums of len 2 subarrays
        for i, (a, b) in enumerate(zip(nums, nums[1:])):
            if a + b in subarray_sums:
                return True
            subarray_sums.add(a + b)

        return False