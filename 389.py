class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_freqs, t_freqs = [0] * 26, [0] * 26
        for letter in s:
            pos = ord(letter) - 97
            s_freqs[pos] += 1
    
        for letter in t:
            pos = ord(letter) - 97
            t_freqs[pos] += 1

        for i, (sf, tf) in enumerate(zip(s_freqs, t_freqs)):
            if sf != tf:  # added letter will appear different number of times
                letter = chr(i + 97)
                return letter