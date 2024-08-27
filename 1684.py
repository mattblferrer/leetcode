class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        consistent = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    break
            else:  # if all letters allowed
                consistent += 1

        return consistent