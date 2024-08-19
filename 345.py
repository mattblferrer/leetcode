class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # convert to list to swap elements
        left, right = 0, len(s) - 1

        while left < right:  # while left and right pointers haven't "met"
            if s[left] in 'aeiouAEIOU':
                while s[right] not in 'aeiouAEIOU':  # find right vowel
                    right -= 1
                s[left], s[right] = s[right], s[left]  # swap vowels
                right -= 1  # move to next right vowel

            left += 1

        return "".join(s)  # convert back to str
