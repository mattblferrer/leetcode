class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_str = bin(n)[2:]
        for a, b in zip(binary_str, binary_str[1:]):
            if a == b:  # adjacent bits are the same, not alternating
                return False
        return True