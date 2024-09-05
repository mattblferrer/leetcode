class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:  # check if minimum of 3 characters
            return False
        for char in '@#$':  # check if includes special characters
            if char in word:
                return False

        word = word.lower()  # lowercase for easier vowel, consonant checking
        for vowel in 'aeiou':  # check for vowels
            if vowel in word:
                break
        else:  # if no vowels found
            return False
        for consonant in 'bcdfghjklmnpqrstvwxyz':  # check for consonants
            if consonant in word:
                break
        else:  # if no consonants found
            return False

        return True   # if all conditions passed, word is valid