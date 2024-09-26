class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums[1:])
        a, b = sorted_nums[0], sorted_nums[1]
        return nums[0] + a + b