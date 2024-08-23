class Solution:
    def minOperations(self, nums: list[int]) -> int:
        prev = 0
        operations = 0

        for num in nums:
            if prev >= num:  # not increasing
                operations += prev - num + 1
                prev += 1
            else:  # increasing
                prev = num
            
        return operations