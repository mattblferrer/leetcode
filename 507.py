class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:  # edge case
            return False

        factor_sum = 1  # include 1 in every number factor sum
        for i in range(2, int(num ** 0.5) + 1):  # sum up factors
            if num % i == 0:
                factor_sum += i + num // i

        return factor_sum == num  # perfect number condition