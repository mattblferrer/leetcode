class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sum_valid = 0
        ctr = 0

        for num in nums:  # even numbers divisible by 3 = divisible by 6
            if num % 6 == 0:
                sum_valid += num
                ctr += 1

        return sum_valid // ctr if ctr != 0 else 0  # get average 