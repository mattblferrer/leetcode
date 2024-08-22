class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        sum_1_digit = sum(num for num in nums if num < 10)
        sum_2_digit = sum(num for num in nums if num > 9)

        return sum_1_digit != sum_2_digit