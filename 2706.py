class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        spent = prices[0] + prices[1]

        if spent > money:  # if no way to buy chocolates with money
            return money
        return money - spent  # money after buying chocolates