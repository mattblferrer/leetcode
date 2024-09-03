class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_num = 0
        leftmost_one = len(s)
        for i, bit in enumerate(s):  # get number of 1 bits in s
            if bit == '1':
                ones_num += 1
                if leftmost_one == len(s):  # get index of leftmost one
                    leftmost_one = i

        # move all 1s to the leftmost bits, while keeping s odd
        return ('1' * (ones_num - 1) + '0' * (len(s) - ones_num) + '1')