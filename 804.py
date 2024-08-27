class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        def toMorseCode(word: str) -> str:
            table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            morse_code = ""
            for letter in word:
                pos = ord(letter) - 97  # a = 0, b = 1, ...
                morse_code += table[pos]

            return morse_code

        unique_transforms = set()  # store unique Morse code transformations
        for word in words:
            morse_code = toMorseCode(word)
            unique_transforms.add(morse_code)

        return len(unique_transforms)