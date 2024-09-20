class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict()

        for i, x in enumerate(nums):
            y = target - x
            if y in nums_dict:
                return [i, nums_dict[y]]
            nums_dict[x] = i
            