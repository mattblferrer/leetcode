class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        def isPrime(num: int) -> bool:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # generate all primes from 2 to 100 (constraint)
        primes = set(i for i in range(2, 101) if isPrime(i))
        for i, n in enumerate(nums):  # find min index where nums[i] prime
            if n in primes:
                min_index = i
                break

        for i, n in enumerate(nums[::-1]):  # if max index, reverse nums
            if n in primes:
                max_index = len(nums) - i - 1
                break

        return max_index - min_index