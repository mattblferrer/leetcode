class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        six_index = -1

        # scan for leftmost 6 to be changed to 9
        for i, digit in enumerate(digits):
            if digit == 6: 
                six_index = len(digits) - i - 1  # since reversed
                break

        # change 6 to 9 and form new number
        maximum = 0
        for i, digit in enumerate(reversed(digits)):
            if i == six_index:
                maximum += 10 ** i * 9
            else: 
                maximum += 10 ** i * digit

        return maximum
    