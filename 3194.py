class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages = []
        while nums:
            minimum, maximum = min(nums), max(nums)
            average = (minimum + maximum) / 2
            averages.append(average)
            nums.remove(minimum)
            nums.remove(maximum)

        return min(averages)