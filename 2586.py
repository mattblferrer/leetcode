class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowel_strings = 0
        for word in words[left:right + 1]:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                vowel_strings += 1

        return vowel_strings