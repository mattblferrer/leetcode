class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()

        # each turn equivalent to swapping elements 2k+1, 2k
        for i in range(0, len(nums), 2):  
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums
    