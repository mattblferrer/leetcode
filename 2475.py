class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        nums.sort()
        length = len(nums)
        triplets = 0

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, length):
                    if nums[i] == nums[k]:
                        continue
                    if nums[j] == nums[k]:
                        continue
                    triplets += 1

        return triplets