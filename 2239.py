class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_num = 1000000
        for num in nums:
            if abs(num) < abs(closest_num):  # closer to zero
                closest_num = num
            if abs(num) == abs(closest_num) and num > 0:  # return larger value
                closest_num = num

        return closest_num