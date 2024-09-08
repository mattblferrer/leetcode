class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = [0] * 26
        uppercase = [0] * 26
        not_special = [0] * 26

        for letter in word:  # check special characters
            if ord(letter) > 96:  # lowercase
                if uppercase[ord(letter) - 97] != 0:  # flag as not special 
                    not_special[ord(letter) - 97] = 1
                else:
                    lowercase[ord(letter) - 97] += 1
            else:  # uppercase
                uppercase[ord(letter) - 65] += 1
        
        special_letters = 0
        for i, (l, u) in enumerate(zip(lowercase, uppercase)):
            if l and u and not not_special[i]:
                special_letters += 1

        return special_letters