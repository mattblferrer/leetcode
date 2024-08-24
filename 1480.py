class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = 0
        arr = []
        for num in nums:
            running_sum += num
            arr.append(running_sum)

        return arr