class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        occurrences = []  # indices of all occurrences of x in nums
        answer = []
        for i, n in enumerate(nums):
            if n == x:
                occurrences.append(i)

        length = len(occurrences)  # number of occurrences of x in nums
        for query in queries:
            if query > length:
                answer.append(-1)
            else:
                answer.append(occurrences[query - 1])  # since 1-indexed

        return answer