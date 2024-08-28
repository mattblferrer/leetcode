class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        frequencies = dict()  # to find n that appears more than once
        for n in nums:
            if n not in frequencies:
                frequencies[n] = 1
            else:  # repeated element found in array
                return n