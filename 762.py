class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]
            return sum(1 for bit in binary_str if bit == '1')

        primes = set([2, 3, 5, 7, 11, 13, 17, 19])  # primes below log2(limit)
        result = 0
        for i in range(left, right + 1):
            if bitCount(i) in primes:
                result += 1

        return result