class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3  # index 0, 1, 2 for red, white, blue freqs
        for num in nums:  # get frequency of colors
            counts[num] += 1

        current_color = 0
        for i in range(len(nums)):  # reconstruct nums according to freq
            while not counts[current_color]:  # move to next color if exhausted
                current_color += 1
            nums[i] = current_color
            counts[current_color] -= 1  

        return nums