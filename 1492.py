class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors1 = []  # factors below sqrt(n)
        factors2 = []  # factors above sqrt(n)

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:  # since i * (n // i) = n
                factors1.append(i)
                if i != n // i:  # avoid adding same factor twice
                    factors2.append(n // i)

        factors2 = factors2[::-1]  # since factors2 in descending order
        factors = factors1 + factors2
        if len(factors) < k:
            return -1
        return factors[k - 1]  # get kth factor (k - 1 since 0-indexed)