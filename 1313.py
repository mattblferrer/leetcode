class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressed = []
        for i, num in enumerate(nums):
            if i % 2 == 0:  # i even
                freq = num
            else:  # i odd
                val = num
                decompressed += [val] * freq

        return decompressed