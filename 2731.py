class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        for i, direction in enumerate(s):  # calculate positions in d seconds
            if direction == 'R':  # positive direction
                nums[i] += d
            else:  # negative direction
                nums[i] -= d
                
        distance = 0
        nums.sort()
        for i in range(len(nums)):  # calculate distance between robot pairs
            distance += i * nums[i] - (len(nums) - i - 1) * nums[i]

        return distance % (10 ** 9 + 7)