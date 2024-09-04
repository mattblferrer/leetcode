class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:  # empty array edge case
            return []

        ranges = []
        start = nums[0]  # start of current range
        length = 0   # length of current range
        for a, b in zip(nums, nums[1:]):
            if b - a == 1:  # check if next number part of range
                length += 1
            else:
                if length == 0:  # if range consists of 1 number
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(start + length))
                start = b
                length = 0

        if length == 0:  # if last range consists of 1 number
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(start + length))
        return ranges