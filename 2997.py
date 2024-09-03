class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]
            return sum(1 for bit in binary_str if bit == '1')

        nums_xor = 0
        for n in nums:  # get bitwise XOR of all elements in array nums
            nums_xor ^= n
        return bitCount(nums_xor ^ k)