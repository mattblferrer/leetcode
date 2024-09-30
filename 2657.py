class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        a_prefix, b_prefix = 0, 0  # bitmasks of present in prefix
        common = []  # prefix common array

        for a, b in zip(A, B):
            a_prefix += 1 << a
            b_prefix += 1 << b
            c = (a_prefix & b_prefix).bit_count()
            common.append(c)

        return common
    