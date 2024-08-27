class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pairs = 0
        for idx, i in enumerate(nums):
            for j in nums[idx+1:]:
                if abs(i - j) == k:
                    pairs += 1

        return pairs