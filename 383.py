class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freqs, mag_freqs = [0] * 26, [0] * 26
        for letter in ransomNote:  # get ransom note letter frequencies
            pos = ord(letter) - 97  # a = 0, b = 1, ...
            ransom_freqs[pos] += 1

        for letter in magazine:  # get magazine letter frequencies
            pos = ord(letter) - 97  # a = 0, b = 1, ...
            mag_freqs[pos] += 1

        for (r, m) in zip(ransom_freqs, mag_freqs):
            if r > m:  # more of specific letter in ransom note than magazine
                return False
        return True