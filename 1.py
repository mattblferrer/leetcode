class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict((v, k) for k, v in enumerate(nums))

        for i, x in enumerate(nums):
            y = target - x
            try:
                j = nums_dict[y]
            except KeyError:
                continue
            if i != j:
                return [i, j]
            