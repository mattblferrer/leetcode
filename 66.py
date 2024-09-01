class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1  # add to ones place (rightmost)

        for i in range(1, len(digits) + 1):
            if digits[-i] != 10:  # check if need to carry 1 to next place
                continue
            digits[-i] = 0
            if i == len(digits):  # if leftmost digit is 9
                digits.insert(0, 1)
                return digits
            digits[-i - 1] += 1

        return digits