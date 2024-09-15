class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        left = 0  # left pointer of substring
        substrings = 0  # number of vowel substrings in word
        length = len(word) 

        while left < length - 4:
            seen_vowels = set()
            right = left  # right pointer of substring

            while right < length:
                if word[right] not in 'aeiou':  # check if consonant
                    break
                seen_vowels.add(word[right])
                if len(seen_vowels) == 5:  # all 5 vowels seen in substring
                    substrings += 1
                right += 1
                
            left += 1
        
        return substrings