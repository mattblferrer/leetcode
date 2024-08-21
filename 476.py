class Solution:
    def findComplement(self, num: int) -> int:
        return (2 ** num.bit_length() - 1) ^ num