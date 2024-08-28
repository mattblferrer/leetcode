from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        frequencies = dict()
        for card in deck:  # count how many times a card appears in the deck
            if card not in frequencies:  # initialize card
                frequencies[card] = 1
            else:
                frequencies[card] += 1
            
        check = frequencies[deck[0]]  # for comparison with other freq values
        for freq in frequencies.values():  # check if all same value
            if gcd(check, freq) == 1:
                return False
            check = gcd(check, freq)
        return True