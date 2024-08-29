from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        beautiful = 0  # number of beautiful pairs
        for i, n1 in enumerate(nums):
            first_digit = [int(d) for d in str(n1)][0]

            for n2 in nums[i + 1:]:
                last_digit = n2 % 10
                if gcd(first_digit, last_digit) == 1:
                    beautiful += 1

        return beautiful