class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        even_cost = 0  # cost to move every coin to even parity
        odd_cost = 0  # cost to move every coin to odd parity
        
        for p in position:
            even_cost += p % 2
            odd_cost += (p + 1) % 2

        return min(even_cost, odd_cost)