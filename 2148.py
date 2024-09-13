class Solution:
    def countElements(self, nums: list[int]) -> int:
        minimum, maximum = min(nums), max(nums)
        count = 0
        for n in nums:
            if n != minimum and n != maximum:
                count += 1
        return count