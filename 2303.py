class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0
        lower = 0

        for bracket in brackets:
            upper, percent = bracket[0], bracket[1] / 100  # unpack bracket
            bracket_size = upper - lower

            if income < bracket_size:  # if income fits in bracket
                tax += income * percent
                break

            # calculate and move to next bracket
            tax += bracket_size * percent
            income -= bracket_size  # size of bracket
            lower = upper  # set new lower bound

        return tax 
    