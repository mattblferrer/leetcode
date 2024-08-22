class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # check if last digit 0 (not 0 itself)
        return num == 0 or num % 10 != 0  