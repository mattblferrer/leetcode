class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)  # list of characters (so that chars can be changed)

        for i in range(len(s) // 2 + 1):
            j = -i - 1  # index of i'th letter counting from right
            left, right = ord(s[i]), ord(s[j])  # get positions in alphabet

            if left < right:  # copy lexicographically smaller letter
                s_list[j] = s_list[i]
            else:
                s_list[i] = s_list[j]

        return "".join(s_list)