class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        nums_set = set(nums)  # for easier searching
        triplets = 0

        for i in range(len(nums)):  # iterate all nums[i], nums[j] pairs
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] < diff:
                    continue
                if nums[j] - nums[i] > diff:  # look through next nums[i]
                    break
                nums_k = nums[j] + diff
                if nums_k in nums_set:
                    triplets += 1

        return triplets