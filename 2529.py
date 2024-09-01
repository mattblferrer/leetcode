class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos, neg = 0, 0
        for i, num in enumerate(nums):
            if num > 0:
                pos += len(nums) - i
                break
            elif num < 0:
                neg += 1

        return max(pos, neg)