class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        lead = digits[0]

        # calculate maximum value Bob can make
        if lead == 9:
            # find first digit that is not 9
            lead_max = 9
            for digit in digits:
                if digit != 9:
                    lead_max = digit
                    break

            max_digits = ["9" if d == lead_max else str(d) for d in digits]
        else:
            max_digits = ["9" if d == lead else str(d) for d in digits]
            
        max_val = int("".join(max_digits))

        # calculate minimum value Bob can make
        min_digits = ["0" if d == lead else str(d) for d in digits]
        min_val = int("".join(min_digits))

        return max_val - min_val
