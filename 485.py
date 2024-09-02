class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive = 0
        consecutive = 0  # current consecutive count
        for n in nums:
            if n:  # 1
                consecutive += 1
            else:  # 0
                if consecutive > max_consecutive:  # get new maximum
                    max_consecutive = consecutive
                consecutive = 0

        if consecutive > max_consecutive:  # if ended in a 1
            max_consecutive = consecutive   
        return max_consecutive