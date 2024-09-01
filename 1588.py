class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        sum_subarrays = 0
        for length in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - length + 1):
                sum_subarrays += sum(arr[i:i + length])

        return sum_subarrays