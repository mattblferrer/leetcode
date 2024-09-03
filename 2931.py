class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        flattened_values = []
        for store in values:  # flatten 2d values list to 1d values list
            for price in store:
                flattened_values.append(price)
        flattened_values.sort()
        
        money = 0
        for d in range(1, len(flattened_values) + 1):
            money += flattened_values[d - 1] * d

        return money