class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]  # convert n from decimal to binary
            return sum(1 for bit in binary_str if bit == '1') 

        sum_values = 0
        for i, num in enumerate(nums):
            if bitCount(i) == k:  # check number of set bits in binary
                sum_values += num

        return sum_values