class Solution:
    def countBits(self, n: int) -> list[int]:
        def bitCount(n: int) -> int:
            binary_str = bin(n)[2:]
            return sum(1 for bit in binary_str if bit == '1')

        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = bitCount(i)

        return ans