class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        frequencies = dict()
        for n in nums:
            if n not in frequencies:
                frequencies[n] = 1
            else:
                frequencies[n] += 1

        sum_unique = 0
        for k, v in frequencies.items():
            if v == 1:  # unique value
                sum_unique += k

        return sum_unique