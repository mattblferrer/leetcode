class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        evens = 0  # only even numbers have trailing zero in binary
        for n in nums:
            if n % 2 == 0:
                evens += 1
            if evens == 2:
                return True
        return False