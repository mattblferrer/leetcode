class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        once = set()
        twice = set()

        for num in nums:  # classify numbers into appearing once and twice
            if num in once:
                twice.add(num)
            else:
                once.add(num)

        xor = 0
        for num in twice:  # get xor of numbers that appeared twice
            xor ^= num
            
        return xor