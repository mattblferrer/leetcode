class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct = set()
        for n in nums:
            distinct.add(n)
            distinct.add(int(str(n)[::-1]))  # reverse digits of n

        return len(distinct)