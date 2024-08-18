class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        output = [0] * len(nums)

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                output[i] += 1 if num > num2 else 0

        return output