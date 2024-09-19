class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        all_indices = dict()
        for i, n in enumerate(nums):  
            if n in all_indices:  # if n already appeared before
                if i - all_indices[n] <= k:  # check if duplicate pair found
                    return True
            all_indices[n] = i

        return False
