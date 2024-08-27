class Solution:
    def minOperations(self, n: int) -> int:
        # get difference of arr[i] from median and add (simplified formula):
        return n * n // 4