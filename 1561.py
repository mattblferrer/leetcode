class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles = sorted(piles, reverse=True)
        max_coins = sum(p for p in piles[1:len(piles) * 2 // 3:2])
        return max_coins