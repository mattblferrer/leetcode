class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i, bit in enumerate(bin(n)[2:][::-1]):  # from biggest to smallest
            if bit == '1':
                reverse += 1 << (31 - i)  # maximum bit value = 2 ** 31

        return reverse