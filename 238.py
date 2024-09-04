class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix, suffix = [1], [1]
        prod = 1
        for n in nums:  # get prefix products of nums as array
            prod *= n
            prefix.append(prod)

        prod = 1
        for n in reversed(nums):  # get suffix products of nums as array
            prod *= n
            suffix.append(prod)

        answer = [prefix[i] * suffix[-i - 2] for i in range(len(nums))]
        return answer