from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def addFraction(f1: tuple[int, int], f2: tuple[int, int]) -> tuple[int, int]:
            n1, d1, n2, d2 = f1[0], f1[1], f2[0], f2[1]  # unpack fractions
            return (n1 * d2) + (n2 * d1), d1 * d2

        def reduceFraction(fraction: tuple[int, int]) -> tuple[int, int]:
            n, d = fraction[0], fraction[1]  # unpack fraction
            reduced_n, reduced_d = n // gcd(n, d), d // gcd(n, d)
            return reduced_n, reduced_d

        def parseExpression(expression: str) -> list[list[int], list[int]]:
            nums, dens = [], []  # numerators, denominators
            current_num = ""

            for char in expression:  # parse expression per character
                if char == "+":
                    dens.append(int(current_num))
                    current_num = ""
                elif char == "-":
                    # check if - not first charcter in expression
                    if current_num != "":  
                        dens.append(int(current_num))
                    current_num = "-"
                elif char == "/":
                    nums.append(int(current_num))
                    current_num = ""
                else:  # digit
                    current_num += char
            dens.append(int(current_num))  # append last denominator 
            return [nums, dens]

        def addFractionsList(nums: list[int], dens: list[int]) -> tuple[int, int]:
            fraction = (0, 1)
            for n, d in zip(nums, dens):
                fraction = reduceFraction(addFraction(fraction, (n, d)))

            return reduceFraction(fraction)

        def fractionToString(fraction: tuple[int, int]) -> str:
            n, d = fraction[0], fraction[1]  # unpack fraction
            return str(n) + "/" + str(d)

        parse_list = parseExpression(expression)
        nums, dens = parse_list[0], parse_list[1]  # numerators, denominators
        fraction_sum = addFractionsList(nums, dens)  # add fractions n/d
        fraction_sum_str = fractionToString(fraction_sum)

        return fraction_sum_str