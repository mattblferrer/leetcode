class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        min_cost = 0
        cost.sort(reverse=True)  # sort cost in descending order

        # get 3 of the most expensive candies at a time
        for set_i in range((len(cost) - 1) // 3 + 1):
            candy_set = cost[set_i * 3:set_i * 3 + 3] 
            if len(candy_set) > 1:  # if more than 1 candy left, sum both
                min_cost += candy_set[0] + candy_set[1]
            else:
                min_cost += candy_set[0]

        return min_cost