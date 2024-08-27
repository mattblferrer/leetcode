class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffled = [""] * len(s)
        for char, index in zip(s, indices):
            shuffled[index] = char
        
        return "".join(char for char in shuffled)