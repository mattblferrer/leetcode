class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.partial_sums = [0] * len(nums)

        partial = 0
        for i, n in enumerate(nums):  # fill in partial sums list
            partial += n
            self.partial_sums[i] = partial

    def sumRange(self, left: int, right: int) -> int:
        return self.partial_sums[right] - self.partial_sums[left] + self.nums[left]