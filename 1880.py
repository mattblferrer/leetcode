class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def numericalValue(word: str) -> int:
            value = ""
            for letter in word:
                pos = ord(letter) - 97  # a = 0, b = 1, c = 2, ... 
                value += str(pos)

            return int(value)

        a = numericalValue(firstWord)
        b = numericalValue(secondWord)
        c = numericalValue(targetWord)
        return a + b == c