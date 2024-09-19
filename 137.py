class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bit_arr = [0] * 32
        for n in nums:
            binary = bin(n % 2**32)[2:]  # convert n to 2s complement (32-bit)
            for i, digit in enumerate(binary[::-1]):  # from right to left
                if digit == '1': 
                    bit_arr[i] += 1

        single = 0  # number which appears exactly once
        for i, digit in enumerate(bit_arr):  
            if digit % 3:  # each number contributes 3x, except for target num
                single += 2 ** i

        return single if single < 2**31 else single - 2**32  # for negative