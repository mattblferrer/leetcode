from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        freq1, freq2 = Counter(words1), Counter(words2)
        strings_num = 0
        for word in words1: 
            if freq1[word] == 1 and freq2[word] == 1:
                strings_num += 1

        return strings_num
