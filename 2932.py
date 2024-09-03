class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums.sort()
        length = len(nums)
        maximum_xor = 0

        for i in range(length - 1):  # test all strong pairs
            for j in range(i + 1, length):
                x, y = nums[i], nums[j]
                if y - x > min(x, y):  # no more strong pairs for given index i
                    continue
                if x ^ y > maximum_xor:
                    maximum_xor = x ^ y

        return maximum_xor