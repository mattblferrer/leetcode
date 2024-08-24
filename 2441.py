class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1

        while left != right:
            if -nums[left] == nums[right]:
                return abs(nums[right])
            elif -nums[left] < nums[right]:
                right -= 1
            else:
                left += 1

        return -1