from math import gcd

class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        nums.sort()
        all_gcd = numsDivide[0]
        for n in numsDivide:  # get gcd of all numbers in numsDivide
            all_gcd = gcd(all_gcd, n)
        
        for i, n in enumerate(nums):
            if all_gcd % n == 0:
                break
            i += 1
        else:  # if no number in nums that divides all elements of numsDivide
            return -1
        return i