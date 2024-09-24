class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]  # list of Fibonacci numbers
        while f[0] < k:  # compute Fibonacci numbers up to constraint
            f.insert(0, f[0] + f[1])  # insert in decreasing order
            
        min_numbers = 0  # min number of Fibonacci that sum to n
        for n in f:
            if k >= n:
                min_numbers += 1
                k -= n

        return min_numbers