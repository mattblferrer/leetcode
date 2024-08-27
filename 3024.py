class Solution:
    def triangleType(self, nums: list[int]) -> str:
        def isTriangle(nums: list[int]) -> bool:
            if nums[0] + nums[1] <= nums[2]:  # triangle inequality
                return False
            if nums[1] + nums[2] <= nums[0]:
                return False
            if nums[2] + nums[0] <= nums[1]:
                return False
            return True

        if not isTriangle(nums): 
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            return "isosceles"
        return "scalene"