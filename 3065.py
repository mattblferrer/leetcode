class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(1 for n in nums if n < k)