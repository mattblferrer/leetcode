class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        all_indices = dict()
        for i, n in enumerate(nums):  # get indices of each element in nums
            if n not in all_indices:
                all_indices[n] = [i]
            else:
                all_indices[n].append(i)

        for n, indices in all_indices.items():
            for i, j in zip(indices, indices[1:]):
                if j - i <= k:
                    return True

        return False
