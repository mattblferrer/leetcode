class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums) 
        averages = set()  # set of distinct averages

        for i in range(n // 2):  # iterate from left and right simultaneously
            a, b = nums[i], nums[n - i - 1]  # a = min, b = max
            averages.add((a + b) / 2)

        return len(averages)