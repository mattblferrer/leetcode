class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        def frequencyArray(word: str) -> list[int]:
            freqs = [0] * 26
            for letter in word:
                pos = ord(letter) - 97  # a = 0, b = 1, ...
                freqs[pos] += 1

            return freqs
        
        # get frequencies of first word as reference
        all_word_freqs = frequencyArray(words[0])
        
        for word in words[1:]:  # update array of all characters in all strings
            freqs = frequencyArray(word)
            for i, (f1, f2) in enumerate(zip(all_word_freqs, freqs)):
                all_word_freqs[i] = min(f1, f2)

        all_chars = []
        for i, f in enumerate(all_word_freqs):  # check letters in all words
            letter = chr(i + 97)   # consider lowercase ASCII position
            all_chars += [letter] * f
        
        return all_chars
