from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def powerset(nums: list[int]) -> int:  # return all subsets of nums
            subsets = []
            for i in range(1, len(nums) + 1):
                subsets += combinations(nums, i)

            return subsets

        xor_sum = 0
        for subset in powerset(nums):
            xor = 0
            for n in subset:
                xor ^= n
            xor_sum += xor

        return xor_sum