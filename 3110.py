class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for char, next_char in zip(s, s[1:]):
            score += abs(ord(char) - ord(next_char))

        return score
