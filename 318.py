class Solution:
    def maxProduct(self, words: list[str]) -> int:
        words_bitmasks = dict()
        max_product = 0
        powers = [2 ** i for i in range(26)]

        for word in words:  # calculate bitmask for every word based on ASCII
            mask_arr = [0] * 26
            mask = 0
            for letter in word:
                mask_arr[ord(letter) - 97] = 1
            for i, n in enumerate(mask_arr):
                if n: 
                    mask += powers[i]
            words_bitmasks[word] = mask

        for i in range(len(words) - 1):  # check every unique pair of words
            for j in range(i + 1, len(words)):
                mask1 = words_bitmasks[words[i]]
                mask2 = words_bitmasks[words[j]]
                if mask1 ^ mask2 == mask1 | mask2:  # do not share letters
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)

        return max_product