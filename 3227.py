class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 0
        for c in s:  # check number of vowels
            if c in 'aeiou':
                vowels += 1

        if vowels == 0:  # no move for Alice, Bob wins
            return False
        return True