class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs = 0

        for i, num_1 in enumerate(nums):
            for j, num_2 in enumerate(nums[i+1:], start=i+1):
                if num_1 == num_2:
                    good_pairs += 1

        return good_pairs