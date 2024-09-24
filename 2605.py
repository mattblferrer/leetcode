class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        nums1_set, nums2_set = set(nums1), set(nums2)
        diff = nums1_set.intersection(nums2_set)  # in common for nums1, nums2
        if len(diff) > 0:  # one digit number contains digit from both arrays
            return min(diff)

        num1, num2 = min(nums1_set), min(nums2_set)
        smaller, larger = min(num1, num2), max(num1, num2)  # two digit number
        return smaller * 10 + larger