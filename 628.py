class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0] < 0 and nums[1] < 0:  # at least two negative
            # check if two negatives multiplied > two positives multiplied 
            if nums[0] * nums[1] * nums[-1] > nums[-1] * nums[-2] * nums[-3]:
                return nums[0] * nums[1] * nums[-1]  
        return nums[-1] * nums[-2] * nums[-3]