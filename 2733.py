class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) < 3:  # no such number
            return -1
        first_three = nums[:3]  # only need to consider first three elements
        return sorted(first_three)[1]