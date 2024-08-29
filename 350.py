class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def returnFrequency(nums: list[str]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1

            return frequencies

        freqs1, freqs2 = returnFrequency(nums1), returnFrequency(nums2)
        intersection = []

        for n, f1 in freqs1.items():  # iterate through n in nums1 for intersection
            if n in freqs2:  
                f2 = freqs2[n]  # get frequency of n in nums2
                i = min(f1, f2)  # frequency in intersection array
                intersection += [n] * i

        return intersection