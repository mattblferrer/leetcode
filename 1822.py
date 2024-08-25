class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1
        for num in nums:  # if positive, don't do anything
            if num == 0:
                return 0
            elif num < 0:  # negative, flip sign
                sign = -sign
            
        return sign