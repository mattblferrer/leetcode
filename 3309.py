from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        binary = [bin(n)[2:] for n in nums]  # convert nums to binary
        maximum_repr = ""
        for p in permutations(binary):
            maximum_repr = max("".join(p), maximum_repr)

        return int(maximum_repr, 2)