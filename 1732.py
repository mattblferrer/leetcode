class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        height, max_height = 0, 0

        for g in gain: 
            height += g
            max_height = max(height, max_height)

        return max_height