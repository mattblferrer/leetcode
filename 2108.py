class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        first = ""
        for word in words:
            if word == word[::-1]:  # palindromic check
                first = word
                break
        
        return first