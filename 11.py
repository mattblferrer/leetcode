class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left != right:
            if height[left] < height[right]:  # move lower wall
                wall_height = height[left]
                left += 1
            else:  # right wall is lower wall
                wall_height = height[right]
                right -= 1

            area = wall_height * (right - left + 1)  # area of rectangle
            if area > max_area:  # check if maximum is reached
                max_area = area

        return max_area