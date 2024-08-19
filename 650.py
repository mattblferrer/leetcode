class Solution:
    def minSteps(self, n: int) -> int:
        factor_sum = 0

        while n % 2 == 0:  # check for 2
            factor_sum += 2
            n //= 2

        if n == 1:  # if n was a power of 2
            return factor_sum
        
        for i in range(3, int(n ** 0.5) + 1, 2):  # odd primes
            while n % i == 0:
                factor_sum += i
                n //= i
            if n == 1:  # break if all prime factors found
                break

        if n != 1:  # if n left after finding small primes, n is also prime
            factor_sum += n
            
        return factor_sum
