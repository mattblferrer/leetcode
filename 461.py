class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]
            return sum(1 for bit in binary_str if bit == '1')
        
        return bitCount(x ^ y)  # Hamming distance definition