class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        seen, ans = [], []
        k = 0
        for n in nums: 
            if n > 0: 
                k = 0  # reset k since n positive
                seen.insert(0, n)
            if n == -1:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)

        return ans