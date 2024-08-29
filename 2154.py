class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2

        return original