class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def convertToArray(num: str) -> list[int]:
            return [int(d) for d in num]

        def addArrays(num1: list[int:], num2: list[int]) -> list[int]:
            if len(num1) < len(num2):  # make num1 the bigger number
                num1, num2 = num2, num1
            num2 = [0] * (len(num1) - len(num2)) + num2  # leading zeros
            array_sum = [d1 + d2 for d1, d2 in zip(num1, num2)]  # add digits

            for i in range(len(array_sum) - 1, -1, -1):  # carry digits > 9
                if array_sum[i] < 10:  # no need to carry
                    continue

                array_sum[i] -= 10
                if i != 0:  # not first digit
                    array_sum[i - 1] += 1
                else:  # first digit
                    array_sum = [1] + array_sum

            return array_sum

        # sum up digits and return sum as str
        arr1, arr2 = convertToArray(num1), convertToArray(num2)
        sum_arr = addArrays(arr1, arr2)
        return "".join(str(digit) for digit in sum_arr)
        