class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        return max(nums2) - max(nums1)