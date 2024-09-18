class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # matrix edge cases
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False

        # binary search in matrix first element
        left, right = 0, m - 1
        while left <= right:
            guess = (left + right) // 2
            if matrix[guess][0] == target:
                return True
            if matrix[guess][0] > target:  # target left of guess
                right = guess - 1
            elif matrix[guess][-1] >= target:  # check if in row interval
                left = guess  # guess is the correct row
                break
            else:  # target right of guess
                left = guess + 1

        row = left
        left, right = 0, n - 1

        # row edge cases
        if matrix[row][-1] < target:  # edge case maximum
            return False
        if matrix[row][0] > target:  # edge case minimum
            return False
        
        # binary search in row
        while left <= right:
            guess = (left + right) // 2
            if matrix[row][guess] == target:
                return True
            if matrix[row][guess] > target:  # target left of guess
                right = guess - 1
            else:  # target right of guess
                left = guess + 1

        return False