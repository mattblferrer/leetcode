class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xor_prefix = [0]
        xor = 0
        for n in arr:
            xor ^= n
            xor_prefix.append(xor)

        return [xor_prefix[l] ^ xor_prefix[r + 1] for l, r in queries]