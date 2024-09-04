class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        nums_or = nums[0]
        for n in nums:
            nums_or |= n
        return nums_or