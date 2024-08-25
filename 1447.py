from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        def reduceFraction(fraction: tuple[int, int]) -> tuple[int, int]:
            n, d = fraction[0], fraction[1]  # unpack fraction
            reduced_n, reduced_d = n // gcd(n, d), d // gcd(n, d)
            return reduced_n, reduced_d

        fractions = set()
        for i in range(1, n + 1):  # create fractions i/j
            for j in range(i + 1, n + 1):
                reduced = reduceFraction((i, j))
                str_reduced = str(reduced[0]) + "/" + str(reduced[1])

                if str_reduced not in fractions:  # filter out duplicates
                    fractions.add(str_reduced)

        return list(fractions)