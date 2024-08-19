class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(account) for account in accounts)