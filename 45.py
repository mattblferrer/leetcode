class Solution:
    def jump(self, nums: list[int]) -> int:
        position = len(nums) - 1  # iterate backwards
        jumps = 0

        while position != 0:  # go from end to start
            for to_jump in range(position):
                # if position can be reached, jump to it
                if nums[to_jump] >= position - to_jump: 
                    position = to_jump
                    jumps += 1
                    break

        return jumps