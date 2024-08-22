class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        left, right = 0, n
        arr = []
        while right < 2 * n:
            arr.append(nums[left])
            arr.append(nums[right])
            left += 1
            right += 1

        return arr