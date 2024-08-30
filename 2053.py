class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        frequencies = dict()
        first_occ = dict()  # first occurrence of s in arr

        for i, s in enumerate(arr):
            if s not in frequencies:
                frequencies[s] = 1
            else:
                frequencies[s] += 1
            if s not in first_occ:
                first_occ[s] = i

        kth_distinct = ""
        ctr = 0  # count number of distinct strings found so far
        for s in first_occ:
            if frequencies[s] > 1:  # not distinct string
                continue
            ctr += 1  
            if ctr == k:  # kth distinct string found
                kth_distinct = s
                break
            
        return kth_distinct