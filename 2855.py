class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        to_shift = nums + nums  # append array to itself
        length = len(nums)

        for i in range(length):  # i = number of left shifts
            shift = to_shift[i:i + length]  # shifted array
            for a, b in zip(shift, shift[1:]):  # check if shift is sorted
                if a > b:
                    break
            else:  # shifted array is sorted, right shift to sort is possible
                return (length - i) % length  # convert to right shifts

        return -1  # not possible