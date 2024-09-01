class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:  # positive x
            is_negative = False
            reverse = str(x)[::-1]  # reverse string
        else:  # negative x
            is_negative = True
            reverse = str(x)[-1:0:-1]  # remove - sign from reverse

        # check if number exceeds 32 bit range
        digits = [int(d) for d in reverse]
        digits_limit = [int(d) for d in str(2 ** 31)]  # negative limit
        digits_limit_pos = [int(d) for d in str(2 ** 31 - 1)]  # positive limit
        if len(digits) < len(digits_limit):  # add leading zeros for comparison
            digits = [0] * (len(digits_limit) - len(digits)) + digits

        if is_negative:
            for d, dl in zip(digits, digits_limit):  # negative limit
                if d > dl:
                    return 0
                if d < dl:
                    break
            return int('-' + reverse)

        for d, dl in zip(digits, digits_limit_pos):  # positive limit
            if d > dl:
                return 0
            if d < dl:
                break
        return int(reverse)