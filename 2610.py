class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1

            return frequencies

        answer = []
        answer_nums = 0  # number of integers already put in answer
        frequencies = returnFrequency(nums)

        while answer_nums != len(nums):  # if integers still left in nums
            current_row = []

            for n, freq in frequencies.items():
                if freq:
                    answer_nums += 1
                    frequencies[n] -= 1
                    current_row.append(n)
            answer.append(current_row)

        return answer