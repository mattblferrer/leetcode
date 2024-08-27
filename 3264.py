class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            minimum = float('inf')
            min_index = -1
            for i, num in enumerate(nums):  # get minimum and index of minimum
                if minimum > num:  # update minimum 
                    minimum = num
                    min_index = i

            nums.pop(min_index)
            nums.insert(min_index, minimum * multiplier)

        return nums