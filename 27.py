class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        right = len(nums) - 1  # pointer counting from the right
        i = 0  # for empty list edge case

        for i, num in enumerate(nums):
            while nums[right] == val:   # make sure val not swapped with itself
                if i >= right:
                    break
                right -= 1 
            if i >= right:  # if pointers meet, all val is removed
                if num != val:  # include current if not to be removed
                    i += 1
                break
            if num == val:
                nums[i], nums[right] = nums[right], nums[i]  # swap elements

        return i