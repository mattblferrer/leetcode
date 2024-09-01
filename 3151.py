class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i, j in zip(nums, nums[1:]):
            if i % 2 == j % 2:
                return False
        return True