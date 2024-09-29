class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        left, right = 0, 0
        substrings = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        curr_vowels = {}
        consonants = 0

        while left < len(word):  # move left pointer all the way to the right
            if word[right] in vowels: # shift right pointer to the right
                if word[right] in curr_vowels:
                    curr_vowels[word[right]] += 1
                else:
                    curr_vowels[word[right]] = 1
            else:
                consonants += 1
            right += 1

            if len(curr_vowels) == 5 and consonants == k:  # count substring
                substrings += 1

            # check if all substrings found for current left pointer
            if right == len(word) or consonants > k:  # reset substring
                curr_vowels = {}
                consonants = 0
                left += 1
                right = left
    
        return substrings
            