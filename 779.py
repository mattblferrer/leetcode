class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:  # return 0 if n = 1, 1 if n = 2
            return k - 1
        if k <= 2 ** (n - 2):  # left of halfway point of current row
            return self.kthGrammar(n - 1, k)
        return 1 ^ self.kthGrammar(n - 1, k - 2 ** (n - 2))  # flip bit