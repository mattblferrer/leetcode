class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        evens = [nums[i] for i in range(0, len(nums), 2)]
        odds = [nums[i] for i in range(1, len(nums), 2)]
        evens.sort()
        odds.sort()
        odds.reverse()

        result = []  # merge back to one array (result)
        for even, odd in zip(evens, odds):
            result.append(even)
            result.append(odd)

        if len(result) != len(nums):  # check if leftover element
            result.append(evens[-1])

        return result