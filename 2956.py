class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer1, answer2 = 0, 0
        nums1_set = set(nums1)  # for faster lookup
        nums2_set = set(nums2)
        for num1 in nums1:
            if num1 in nums2_set:
                answer1 += 1
        
        for num2 in nums2:
            if num2 in nums1_set:
                answer2 += 1

        return [answer1, answer2]