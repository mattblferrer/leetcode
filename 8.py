class Solution:
    def myAtoi(self, s: str) -> int:
        result_str = ""  # filter out non-integer characters first
        s = s.lstrip()  # remove leading whitespace

        if not s:  # if empty string
            return 0

        # check signedness
        if s[0] == "-":
            is_negative = True
            s = s[1:]  # remove sign
        elif s[0] == "+":
            is_negative = False
            s = s[1:]  # remove sign
        else:
            is_negative = False

        # conversion
        for char in s:
            if char.isdigit():
                result_str += char
            else:
                break

        if result_str == '':  # if no digits read, result is 0
            return 0

        # cast valid num string to integer
        result = -int(result_str) if is_negative else int(result_str)

        # rounding
        if result > (2 ** 31 - 1):
            result = 2 ** 31 - 1
        elif result < -(2 ** 31):
            result = -(2 ** 31)

        return result

