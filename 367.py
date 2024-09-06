class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:  # edge case
            return True

        left, right = 0, num  # initial guess
        while left <= right:
            guess = (left + right) // 2
            square = guess * guess
            if square == num:  # square root found
                return True
            if square > num:
                right = guess - 1
            elif square < num: 
                left = guess + 1

        return False