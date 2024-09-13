class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        def isIncreasing(nums: list[int]) -> bool:
            for a, b in zip(nums, nums[1:]):
                if a > b: 
                    return False
            return True
        
        def isDecreasing(nums: list[int]) -> bool:
            for a, b in zip(nums, nums[1:]):
                if a < b: 
                    return False
            return True

        return isIncreasing(nums) or isDecreasing(nums)