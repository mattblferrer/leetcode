class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = [0] * 26
        uppercase = [0] * 26

        for letter in word:  # check special characters
            if ord(letter) < 96:  # uppercase
                uppercase[ord(letter) - 65] += 1
            else:  # lowercase
                lowercase[ord(letter) - 97] += 1
        
        special_letters = 0
        for l, u in zip(lowercase, uppercase):  # check if letter is special
            if l and u:
                special_letters += 1

        return special_letters