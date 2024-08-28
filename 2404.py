class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        frequencies = dict()
        for n in nums:  # count number of times each n appears
            if n not in frequencies:  # initialize value of n 
                frequencies[n] = 1
            else:
                frequencies[n] += 1

        freq_n, max_freq = -1, 0
        for n, freq in frequencies.items():
            if n % 2 != 0:  # don't check if odd
                continue
            if freq < max_freq:  # less frequent, ignore
                continue   
            if freq == max_freq:  # same frequency, return smallest 
                if n < freq_n:
                    freq_n = n
            else:  # more frequent, replace previous most frequent element
                freq_n = n
                max_freq = freq
        
        return freq_n