# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        guess = (left + right) // 2

        while left < right:
            guess = (left + right) // 2
            if isBadVersion(guess):  # type: ignore # retain right as bad version
                right = guess
            else:
                left = guess + 1

        return right