class Solution:
    def countAsterisks(self, s: str) -> int:
        is_pair = False
        asterisks = 0
        for char in s:
            if char == "|":  # create or delete pair
                is_pair = not is_pair
            elif char == "*" and not is_pair:
                asterisks += 1

        return asterisks