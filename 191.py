class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]
        return sum(1 for bit in binary_str if bit == '1') 