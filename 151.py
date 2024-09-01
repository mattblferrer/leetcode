class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # remove leading, trailing space
        words = s.split(" ")[::-1]  # get words as list and reverse order
        reverse_str = ""
        for word in words:
            if word:  # check if word is not space
                reverse_str += word + " "
        
        return reverse_str[:-1]  # remove trailing space
