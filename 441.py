class Solution:
    def arrangeCoins(self, n: int) -> int:
        initial = int(n ** 0.5) * 2  # initial guess (that's always over)
        for guess in range(initial, 0, -1):
            coins = guess * (guess + 1) // 2
            if coins <= n:  # first time it crosses under
                return guess

        return 1