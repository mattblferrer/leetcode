class Solution:
    def check(self, nums: list[int]) -> bool:
        minimum = float('inf')

        for i, n in enumerate(nums):  # find minimum and minimum index
            if n < minimum:
                minimum = n
                min_i_list = [i]
            elif n == minimum:
                min_i_list.append(i)

        sorted_nums = sorted(nums)
        length = len(nums)
        for min_index in min_i_list:
            for i, n in enumerate(sorted_nums):  # check sorted array if rotated
                if nums[(i + min_index) % length] != n:  # out of order
                    break
            else:  # if no elements out of order = rotated array
                return True

        return False