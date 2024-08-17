class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:  # base case
            return 0

        is_prime = [True] * n  # sieve out primes 
        
        # for prime 2
        if n > 3:
            for i in range(4, n, 2):
                is_prime[i] = False

        # for odd primes
        for k in range(3, int(n ** 0.5) + 1, 2):
            for i in range(k * 2, n, k):
                is_prime[i] = False

        # count number of primes
        return sum(is_prime) - 2  # not counting 0, 1
        