class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        pairs = 0
        for i, num in enumerate(nums):
            for num2 in nums[i+1:]:
                if num + num2 < target:
                    pairs += 1
                
        return pairs