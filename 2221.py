class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for a, b in zip(nums, nums[1:]):  # iterate over adjacent elements
                new_nums.append((a + b) % 10)

            nums = new_nums

        return nums[0]