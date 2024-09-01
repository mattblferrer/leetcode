class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:  # not possible
            return []
        return [num // 3 - 1, num // 3, num // 3 + 1]