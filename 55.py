class Solution:
    def canJump(self, nums: list[int]) -> bool:
        distance = 0
        position = len(nums) - 1  # start from right 

        while position - distance >= 0:  # iterate through all nums in reverse
            if nums[position - distance] >= distance:  # found closer position
                position -= distance
                distance = 0
            distance += 1
            if position == 0:   # reached position 0 (first index)
                return True

        return False