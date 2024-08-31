class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for i in range(0, len(nums) // 2):
                if i % 2 == 0:  # even index, get minimum
                    newNums.append(min(nums[2*i], nums[2*i + 1]))
                else:  # odd index, get maximum
                    newNums.append(max(nums[2*i], nums[2*i + 1]))
            nums = newNums

        return nums[0]