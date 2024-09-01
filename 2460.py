class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):  # first operation
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        result = []
        for n in nums:  # shift all zeros = shift nonzeros to start of array
            if n != 0:
                result.append(n)
        result += [0] * (len(nums) - len(result))  # shift zeros to end
        return result