class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for num in nums:
                if num not in frequencies:
                    frequencies[num] = 1
                else:
                    frequencies[num] += 1
            
            return frequencies

        frequencies = returnFrequency(nums)
        for f in frequencies.values():  # check if all frequencies even
            if f % 2 == 1:
                return False
        return True