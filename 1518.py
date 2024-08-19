class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full, empty, drank = numBottles, 0, 0  # initial condition

        while full:  # drink and exchange for bottles
            full, empty, drank = 0, empty + full, drank + full  # drink
            full, empty = empty // numExchange, empty % numExchange  # exchange

        return drank
    