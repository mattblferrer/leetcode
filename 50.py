class Solution:
    # Implementation of exponentiation by squaring
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n > 0:  # positive power
            if n % 2 == 1:  # if n odd
                return x * self.myPow(x * x, n // 2)
            else:  # if n even
                return self.myPow(x * x, n // 2)      

        else:  # negative power
            return self.myPow(1 / x, abs(n))
