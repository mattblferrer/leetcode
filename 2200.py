class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        indices = set()  # set of distinct k-distant indices
        for i, n in enumerate(nums):
            if n == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    indices.add(j)  # add all indices with distance < k from n

        return sorted(list(indices))  # return in increasing order