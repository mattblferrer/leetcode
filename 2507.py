class Solution:
    def smallestValue(self, n: int) -> int:
        def sumOfPrimeFactors(n: int) -> int:
            prime_sum = 0  # sum of prime factors
            while n % 2 == 0:  # check only even prime
                prime_sum += 2
                n //= 2
            
            for i in range(3, int(n ** 0.5) + 1, 2):  # odd primes
                while n % i == 0:
                    prime_sum += i
                    n //= i
                if n < int(n ** 0.5) + 1:  # no need to check past this point
                    break

            if n > 1:  # if remaining n is a prime factor itself
                prime_sum += n
            return prime_sum

        prime_sum = n
        while True:
            n = prime_sum
            prime_sum = sumOfPrimeFactors(n)
            if prime_sum == n:  # check if n is a prime
                break

        return prime_sum