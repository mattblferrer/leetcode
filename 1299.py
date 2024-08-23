class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1
        answer = []

        for num in reversed(arr):
            answer.append(maximum)
            if num > maximum:  # update maximum 
                maximum = num

        return reversed(answer)