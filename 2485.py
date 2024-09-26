class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = n * (n + 1) // 2
        i = 1  # current integer to add

        while left_sum < right_sum:
            left_sum += i
            if left_sum == right_sum:  # pivot integer found, return i
                return i
            right_sum -= i
            i += 1

        return -1  # no such pivot integer 