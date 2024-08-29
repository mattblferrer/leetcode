class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:  # edge case if no cuts are needed
            return 0 
        return n if n % 2 == 1 else n // 2