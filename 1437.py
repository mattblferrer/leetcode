class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        ctr = 0  # counter of distance from last 1 found
        seen_one = False  # if the first 1 has been seen in array

        for n in nums:
            if not seen_one:  # first 1, no distance check needed
                if n == 1:
                    seen_one = True
                continue
            if n == 0:
                ctr += 1
            else:
                if ctr < k:
                    return False 
                ctr = 0  # reset distance counter

        return True