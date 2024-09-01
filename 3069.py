class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1, arr2 = [nums[0]], [nums[1]]  
        for i, num in enumerate(nums[2:], start=2):
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)

        return arr1 + arr2