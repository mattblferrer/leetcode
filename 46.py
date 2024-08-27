class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:  # base case or end of permutation
            return [nums]
        
        # iterate through possible next elements of permutation
        permutations = []
        for i, num in enumerate(nums):  
            nums_c = nums[:]  # copy of nums
            nums_c.pop(i)  # put num to front of permutation
            permutations += [[num] + p for p in self.permute(nums_c)]

        return permutations