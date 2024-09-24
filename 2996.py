class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        prefix_sum = nums[0]
        nums_set = set(nums)

        for a, b in zip(nums, nums[1:]):  # find longest sequential prefix
            if b - a != 1:
                break
            prefix_sum += b

        x = prefix_sum
        while True:  # find smallest x >= prefix_sum missing from nums
            if x not in nums_set:
                return x
            x += 1
