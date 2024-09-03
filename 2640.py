class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        maximum = 0
        conver = []
        score = []
        score_sum = 0

        for i, n in enumerate(nums):
            if n > maximum:  # update maximum
                maximum = n
            conver.append(n + maximum)
            score_sum += n + maximum
            score.append(score_sum)

        return score
