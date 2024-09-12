from random import randint

class Solution:

    def __init__(self, nums: list[int]):
        self.freqs = dict()
        for i, n in enumerate(nums):
            if n not in self.freqs:
                self.freqs[n] = [i]
            else:
                self.freqs[n].append(i)

    def pick(self, target: int) -> int:
        rand = randint(0, len(self.freqs[target]) - 1)
        return self.freqs[target][rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)