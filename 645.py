class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()
        sum_expected = n * (n + 1) // 2
        sum_actual = sum(nums)
        for num in nums:
            if num in seen:
                duplicated = num
                break
            seen.add(num)

        missing = (sum_expected + duplicated) - sum_actual
        return [duplicated, missing]