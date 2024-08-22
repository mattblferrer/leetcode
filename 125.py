class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # convert to lowercase
        char_list = []
        for char in s:  # remove non-alphanumeric characters
            if char.isalpha() or char.isdigit():
                char_list.append(char)
                
        return char_list == char_list[::-1]  # check if palindrome