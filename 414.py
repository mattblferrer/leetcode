class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))  # remove duplicates
        nums.sort()
        return nums[-3] if len(nums) > 2 else nums[-1]