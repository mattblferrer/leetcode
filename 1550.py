class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        odds = 0
        for num in arr:
            if num % 2 == 1:
                odds += 1
            else:
                odds = 0
            if odds == 3:
                return True

        return False