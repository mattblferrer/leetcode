class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(cost)
        gas_cost = [0] * n
        curr_cost = 0
        start = 0
        min_gc_diff = float('inf')
        
        # start on station with most gas needed to travel to
        for i, (g, c) in enumerate(zip(gas, cost)):
            curr_cost += g - c
            gas_cost[i] = curr_cost

            if curr_cost < min_gc_diff:  # update minimum
                min_gc_diff = curr_cost
                start = (i + 1) % n

        curr_gas = gas[start]  # initial fillup of gas
        for i in range(start, start + n + 1):
            curr_gas -= cost[i % n]  # travel to next station
            if curr_gas < 0:  # ran out of gas
                return -1
            curr_gas += gas[(i + 1) % n]  # refill gas
        
        return start
            
            