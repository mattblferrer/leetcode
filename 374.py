# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n + 1
        next_guess = (low + high) // 2

        while low != high:  # if equal, that means number found
            next_guess = (low + high) // 2

            if guess(next_guess) == -1:  # type: ignore # guess is higher than the number
                high = next_guess
            elif guess(next_guess) == 1:  # type: ignore # guess is lower than the number
                low = next_guess
            else:  # guess is equal to the number
                break

        return next_guess