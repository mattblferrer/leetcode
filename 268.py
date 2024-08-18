class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i, num in enumerate(sorted(nums)):
            if i != num:
                return i

        return len(nums)