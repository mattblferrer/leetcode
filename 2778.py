class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        sum_of_squares = 0
        for i, num in enumerate(nums, start=1):
            if len(nums) % i == 0:
                sum_of_squares += num * num

        return sum_of_squares