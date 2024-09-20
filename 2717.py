class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        for i, x in enumerate(nums):  # find indices of 1 and n
            if x == n:
                index_n = i
            elif x == 1:
                index_1 = i

        # subtract 1 swap since (1, n) swap in the middle at the same time
        if index_n < index_1:  
            return index_1 + (n - index_n - 2) 
        return index_1 + (n - index_n - 1)  # no (1, n) swap