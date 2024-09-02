class Solution:
    def binaryGap(self, n: int) -> int:
        one_bits = dict()  # index of positions of bits where bit = 1
        binary_str = bin(n)[2:]
        for i, bit in enumerate(binary_str):  # get 1 bit indices
            if bit == '0':
                continue
            if 1 not in one_bits:
                one_bits[1] = [i]
            else:
                one_bits[1].append(i)

        max_distance = 0
        for a, b in zip(one_bits[1], one_bits[1][1:]):  # adjacent bit indices
            if b - a > max_distance:
                max_distance = b - a

        return max_distance