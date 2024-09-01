class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        power = 0
        even, odd = 0, 0  # even and odd bits counter
        while n > 0:
            if n % 2 == 1:  # bit at index (power)
                if power % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n //= 2
            power += 1

        return [even, odd]