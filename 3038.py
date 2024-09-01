class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        score = nums[0] + nums[1]  # for comparison
        steps = 1
        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] != score:
                break
            steps += 1
        return steps