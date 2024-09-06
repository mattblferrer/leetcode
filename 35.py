class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # left and right pointers
        if nums[right] < target:  # if greater than all elements
            return right + 1
        if nums[left] >= target:  # if less than all elements
            return 0

        while left <= right:  # binary search
            guess = (left + right) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess] > target:  # target to the left of guess
                right = guess - 1
            elif nums[guess] < target:  # target to the right of guess
                left = guess + 1

        return left  # return insert position if element not found