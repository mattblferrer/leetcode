class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        nums_sets = [set(subset) for subset in nums]
        present = []  # intersection of arrays in nums
        for n in nums[0]:
            for subset in nums_sets:
                if n not in subset:
                    break
            else:
                present.append(n)

        return sorted(present)