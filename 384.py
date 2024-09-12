from random import randint

class Solution:

    def __init__(self, nums: list[int]):
        self.arr = nums

    def reset(self) -> list[int]:
        return self.arr

    def shuffle(self) -> list[int]:
        original = self.arr[:]  # create copy of original array
        shuffled = []  # shuffled array
        for i in range(len(original) - 1, -1, -1):
            rand = randint(0, i)  # choose random element from array
            shuffled.append(original[rand])
            original.pop(rand)

        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()