class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens = sorted([num for num in nums if num % 2 == 0])
        odds = sorted([num for num in nums if num % 2 == 1])

        answer = []  # construct new array from alternating even, odd
        for e, o in zip(evens, odds): 
            answer.append(e)
            answer.append(o)

        return answer