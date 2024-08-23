class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        product = 1
        sum_digits = 0
        for d in digits:  # calculate product
            product *= d
            sum_digits += d

        return product - sum_digits