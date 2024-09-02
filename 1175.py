class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):  # odd primes
                if n % i == 0:
                    return False
            return True

        def factorial(n: int) -> int:
            fac = 1
            for i in range(1, n + 1):
                fac *= i
            return fac

        primes = sum(1 for i in range(n + 1) if isPrime(i))
        return (factorial(primes) * factorial(n - primes)) % (10 ** 9 + 7)