class Solution:
    # implementation of Newton-Raphson method
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        guess = x / 2  # initial guess

        # approximation loop
        for _ in range(20):
            guess = 0.5 * (guess + x / guess)

        return int(guess)
    