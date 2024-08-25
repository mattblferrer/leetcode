class Solution:
    def isThree(self, n: int) -> bool:
        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2 or num == 3:  # for 2 and 3
                return True
            if num % 2 == 0 or num % 3 == 0:  # for 2 and 3
                return False

            for i in range(6, int(num ** 0.5) + 3, 6):  # for 6k +- 1
                if num % (i - 1) == 0:
                    return False
                if num % (i + 1) == 0:
                    return False
            return True

        # return True if square of a prime, else False
        if (int(n ** 0.5)) ** 2 == n:  # square check
            return isPrime(int(n ** 0.5))
        return False