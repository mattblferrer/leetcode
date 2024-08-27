class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:  # edge case
            return True

        left, right = 0, num  # initial guess

        while left != right and left != right - 1:
            guess = (left + right) // 2
            square = guess * guess
            if square == num:  # square root found
                return True
            if square > num:
                right = guess
            elif square < num: 
                left = guess

        return False