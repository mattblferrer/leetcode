class Bank:

    def __init__(self, balance: list[int]):
        self.balance = [0] + balance  # make array 0-indexed
        self.length = len(balance)  # index of last element in balance array

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.length or account2 > self.length:  
            return False
        if self.balance[account1] < money:  # not enough in origin account
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.length:  # check if account exists
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.length:  # check if account exists
            return False
        if self.balance[account] < money:  # not enough in origin account
            return False
        self.balance[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)