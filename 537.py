class Solution:
    def stringToComplex(self, num: str) -> tuple[int, int]:
        add_pos = num.index("+")  # search for addition symbol
        real_part = int(num[:add_pos])
        complex_part = int(num[add_pos+1:-1])

        return real_part, complex_part

    def complexToString(self, real_part: int, complex_part: int) -> str:
        return str(real_part) + "+" + str(complex_part) + "i"

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_r, num1_c = self.stringToComplex(num1)
        num2_r, num2_c = self.stringToComplex(num2)

        # complex multiplication 
        real_part = num1_r * num2_r - num1_c * num2_c
        complex_part = num1_r * num2_c + num1_c * num2_r

        # conversion to output string
        return self.complexToString(real_part, complex_part)