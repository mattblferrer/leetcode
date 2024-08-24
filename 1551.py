class Solution:
    def minOperations(self, n: int) -> int:
        # get difference of arr[i] from median and add (simplified formula):
        if n % 2 == 0:  # even
            return n * n // 4
        return (n // 2) * (n // 2 + 1)  # odd