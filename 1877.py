class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_pair_sum = 0
        for a, b in zip(nums[:len(nums) // 2], nums[len(nums) // 2:][::-1]):
            max_pair_sum = max(max_pair_sum, a + b)

        return max_pair_sum