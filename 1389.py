class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i, num in zip(index, nums):
            target.insert(i, num)

        return target