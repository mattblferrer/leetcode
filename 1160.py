class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        def returnFrequency(word: str) -> dict[str, int]:
            frequencies = dict()
            for letter in word:
                if letter not in frequencies:
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1

            return frequencies
        
        chars_freq = returnFrequency(chars)
        total_length = 0

        for word in words:  # check if words can be formed by characters
            word_freq = returnFrequency(word)

            # if letter more frequent in word than chars, then cannot be formed
            for letter, f in word_freq.items():
                if letter not in chars_freq:
                    break
                if chars_freq[letter] < f:
                    break
            else:
                total_length += len(word)
        
        return total_length