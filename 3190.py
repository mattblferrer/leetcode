class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 != 0:  # if 1 mod 3, subtract, if 2 mod 3, add
                operations += 1

        return operations