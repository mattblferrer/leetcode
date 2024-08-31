class Solution:
    def stringHash(self, s: str, k: int) -> str:
        hash_string = ""
        for i in range(len(s) // k):
            substr = s[i * k: i * k + k]  # divide s into substrings of n // k 
            hash_sum = 0
            for c in substr:  # get characters and sum up hash
                c_hash = ord(c) - 97
                hash_sum += c_hash
            
            hashed = chr((hash_sum % 26) + 97)
            hash_string += hashed

        return hash_string