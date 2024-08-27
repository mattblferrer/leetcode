class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def permute(nums: list[int]) -> list[list[int]]:
            if len(nums) == 1:  # base case or end of permutation
                return [nums]
            
            # iterate through possible next elements of permutation
            permutations = []
            for i, num in enumerate(nums):  
                nums_c = nums[:]  # copy of nums
                nums_c.pop(i)  # put num to front of permutation
                permutations += [[num] + p for p in permute(nums_c)]

            return permutations

        permutations = permute(nums)  # generate permutations with duplicate
        permute_unique = []
        for p in permutations:  # remove duplicates
            if p not in permute_unique:
                permute_unique.append(p)

        return permute_unique