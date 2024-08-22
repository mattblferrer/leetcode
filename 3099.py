class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        return sum(int(d) for d in str(x)) if x % sum(int(d) for d in 
            str(x)) == 0 else -1