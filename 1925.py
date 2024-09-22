from math import gcd

class Solution:
    def countTriples(self, n: int) -> int:
        triples = 0

        for x in range(1, n):
            for y in range(x + 1, n):
                if gcd(x, y) != 1:  # not coprime (Euclid's formula constraint)
                    continue
                if x % 2 == 1 and y % 2 == 1:  # at least one x, y even 
                    continue
                    
                a = y*y - x*x
                b = 2*x*y
                c = y*y + x*x
                if c > n:  # stop checking y, no new triple will be found
                    break
                while c <= n: 
                    triples += 2  # account for pairs (a, b, c), (b, a, c)
                    c += y*y + x*x

        return triples