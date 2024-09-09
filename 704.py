class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:  # check only element in nums array
            return 0 if nums[0] == target else -1

        left, right = 0, len(nums)
        while left != right:
            guess = (left + right) // 2
            if nums[guess] == target:
                return guess
            if nums[guess] < target:  # target to the right of guess
                left = guess + 1
            else:  # target to the left of guess
                right = guess 
         
        return -1  # target not found 