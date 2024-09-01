class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return min(numOnes, k) - min(numNegOnes, max(k - numOnes - numZeros, 0))