from math import gcd

class Solution:
    def countTriples(self, n: int) -> int:
        triples = 0

        for x in range(1, n):
            for y in range(x + 1, n):
                if gcd(x, y) != 1:  # not coprime (Euclid's formula constraint)
                    continue
                if x % 2 == 1 and y % 2 == 1:
                    continue
                    
                a = y ** 2 - x ** 2
                b = 2 * x * y
                c = y ** 2 + x ** 2
                if c > n:  # stop looping, no triple below limit will be found
                    break
                while c <= n: 
                    triples += 2  # account for pairs (a, b, c), (b, a, c)
                    c += y ** 2 + x ** 2

        return triples