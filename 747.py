class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_idx = nums.index(max(nums))
        maximum = nums.pop(max_idx)
        second_idx = nums.index(max(nums))
        second = nums.pop(second_idx)

        return max_idx if maximum >= 2 * second else -1
