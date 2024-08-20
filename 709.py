class Solution:
    def toLowerCase(self, s: str) -> str:
        lowercase = []
        for char in s:
            if 64 < ord(char) < 91:  # detect uppercase
                lowercase.append(chr(ord(char) + 32))
            else:  # lowercase
                lowercase.append(char)

        return "".join(lowercase)
    