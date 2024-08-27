class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        score = 0
        for _ in range(k):
            maximum = max(nums)  # step 1
            nums.remove(maximum)  # step 2
            nums.append(maximum + 1)  # step 3
            score += maximum  # step 4

        return score