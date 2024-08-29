class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        present = set()  # with values present in at least two arrays (or sets)

        for n in set1:
            if n in set2 or n in set3:
                present.add(n)
        for n in set2:
            if n in set3 or n in set1:
                present.add(n)
        for n in set3:
            if n in set1 or n in set2:
                present.add(n)

        return list(present)  # return as list