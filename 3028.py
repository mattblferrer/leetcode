class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        position = 0
        returns = 0

        for num in nums:
            position += num

            if position == 0:  # check if on boundary
                returns += 1

        return returns
    