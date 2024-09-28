class Solution:
    def minElement(self, nums: list[int]) -> int:
        sum_digits = [sum(int(d) for d in str(num)) for num in nums]
        return min(sum_digits)