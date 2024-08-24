class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_2 = 0
        for ptr_1 in range(m, m + n):  # iterate through 0s in original nums1
            nums1[ptr_1] = nums2[ptr_2]
            swap = ptr_1

            # swap elements until newly inserted element is in right place
            while swap > 0 and nums1[swap - 1] > nums2[ptr_2]:
                nums1[swap], nums1[swap - 1] = nums1[swap - 1], nums1[swap]
                swap -= 1

            ptr_2 += 1

        return nums1