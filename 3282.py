class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        max_score = [0] * len(nums)
        max_found = 0
        
        for i, n in enumerate(nums):
            if i > 0:  # update next index with max score
                max_score[i] = max_score[i - 1] + max_found
            if n > max_found:  # update maximum score found so far 
                max_found = n

        return max_score[-1]  # score at end of array
