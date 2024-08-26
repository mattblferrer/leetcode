class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num
            digit_sum += sum(int(d) for d in str(num))

        return abs(element_sum - digit_sum)