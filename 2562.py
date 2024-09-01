class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        concat_value = 0
        for i in range(len(nums) // 2):
            concat = int(str(nums[i]) + str(nums[-i - 1]))
            concat_value += concat

        if len(nums) % 2 == 1:  # if odd length, add median element
            concat_value += nums[len(nums) // 2]
        return concat_value