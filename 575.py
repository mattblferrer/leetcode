class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        total_candies = len(candyType)
        types = len(set(candyType)) 
        return min(types, total_candies // 2)