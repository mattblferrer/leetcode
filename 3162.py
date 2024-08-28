class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        good_pairs = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 % (num2 * k) == 0:
                    good_pairs += 1

        return good_pairs