class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1  # left, right pointers
        sorted_arr = []

        # sort in reverse order (non-increasing order)
        while left <= right:  # check if all numbers in nums seen
            if abs(nums[left]) > abs(nums[right]):
                sorted_arr.append(nums[left] * nums[left])
                left += 1
            else:
                sorted_arr.append(nums[right] * nums[right])
                right -= 1

        return reversed(sorted_arr)