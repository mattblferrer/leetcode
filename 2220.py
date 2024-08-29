class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]  # convert n from decimal to binary
            return sum(1 for bit in binary_str if bit == '1') 

        return bitCount(start ^ goal)