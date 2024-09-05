class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n_bits = [i for i, bit in enumerate(bin(n)[2:][::-1]) if bit == '1']
        k_bits = [i for i, bit in enumerate(bin(k)[2:][::-1]) if bit == '1']
        n_set, k_set = set(n_bits), set(k_bits)

        for index in k_bits:
            if index not in n_set:  # impossible to change bit from 0 to 1
                return -1

        bits_changed = 0
        for index in n_bits:
            if index not in k_set:  
                bits_changed += 1  # change 1 to 0
                
        return bits_changed