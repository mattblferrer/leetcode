class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full, empty, drank = numBottles, 0, 0  # initial condition

        while full:  # drink and exchange for bottles
            full, empty, drank = 0, empty + full, drank + full  # drink

            while empty >= numExchange:  # exchange
                full, empty = full + 1, empty - numExchange  
                numExchange += 1

        return drank
