class Solution:
    def longestPalindrome(self, s: str) -> int:
        def returnFrequency(s: str) -> dict[str, int]:
            frequencies = dict()
            for letter in s:
                if letter not in frequencies:
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1

            return frequencies
        
        s_freqs = returnFrequency(s)
        max_length = 0  # length of longest palindrome
        has_middle = False

        for freq in s_freqs.values():
            if freq % 2 == 0:  # even frequency
                max_length += freq 
                continue
            if not has_middle:
                max_length += 1
                has_middle = True
            max_length += (freq - 1)

        return max_length