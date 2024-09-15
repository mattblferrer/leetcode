class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        twice = []
        for n in nums:
            if n in seen:
                twice.append(n)
            seen.add(n)

        return twice