class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isCase1(word: str) -> bool:  # all uppercase
            for char in word:
                if not char.isupper():
                    return False
            return True
        
        def isCase2(word: str) -> bool:  # all lowercase
            for char in word:
                if not char.islower():
                    return False
            return True

        def isCase3(word: str) -> bool:  # only first letter uppercase
            if word[0].islower():
                return False
            for char in word[1:]:
                if char.isupper():
                    return False
            return True

        return isCase1(word) or isCase2(word) or isCase3(word)