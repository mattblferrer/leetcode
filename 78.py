class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        power_set = []
        for i in range(2 ** len(nums)):
            binary = bin(i)[2:]  # binary index defines a unique subset
            subset = []
            for j, digit in enumerate(reversed(binary)):
                if digit == "1":  # include element in index j of nums
                    subset.append(nums[j])
            
            power_set.append(subset)

        return power_set
    