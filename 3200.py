class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        height = 0
        red_temp, blue_temp = red, blue  # to decrement red, blue
        while red_temp >= 0 and blue_temp >= 0:  # if red ball on top
            height += 1
            if height % 2 == 0:
                blue_temp -= height
            else:
                red_temp -= height

        max_height = height
        height = 0
        while red >= 0 and blue >= 0:  # if blue ball on top
            height += 1
            if height % 2 == 1:
                blue -= height
            else:
                red -= height

        return max(max_height, height) - 1  # except last row (incomplete)