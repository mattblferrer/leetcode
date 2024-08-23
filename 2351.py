class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeared = set()
        for letter in s:
            if letter in appeared:
                return letter
            appeared.add(letter)