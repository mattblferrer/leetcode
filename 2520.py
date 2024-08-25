class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for d in [int(d) for d in str(num)] if num % d == 0)