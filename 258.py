class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:  # more than 1 digit
            num_copy = num
            num = 0  # sum of digits

            while num_copy > 0:  # get digits of num
                num_copy, digit = divmod(num_copy, 10)
                num += digit

        return num
    