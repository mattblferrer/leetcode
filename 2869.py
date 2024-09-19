class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collection = set()  # collection of elements 1, 2, ... k
        i = 0
        while len(collection) < k:
            i += 1
            if nums[-i] <= k:
                collection.add(nums[-i])

        return i