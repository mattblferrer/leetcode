from math import gcd

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        all_gcd = nums[0]
        for n in nums:
            all_gcd = gcd(all_gcd, n)
        return all_gcd == 1