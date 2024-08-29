class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_index = 0  # index of row with maximum count of ones
        max_count = 0  # maximum count of ones

        for i, row in enumerate(mat):
            count = sum(row)
            if count > max_count:
                max_index = i
                max_count = count

        return [max_index, max_count]