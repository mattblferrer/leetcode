class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # equivalent to checking if n has no 2s in ternary representation
        while n > 0:
            if n % 3 == 2: 
                return False
            n //= 3
        return True