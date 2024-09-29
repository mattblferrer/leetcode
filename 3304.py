class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) <= k:
            add_word = ""
            for c in word:
                if c == "z":
                    add_word += "a"
                else:
                    add_word += chr(ord(c) + 1)  # next character
            word += add_word
        
        return word[k - 1]