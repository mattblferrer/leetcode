class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(n for n in nums if n != 0))