class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sorted_heights = sorted(heights)
        indices = 0
        for h1, h2 in zip(heights, sorted_heights):
            if h1 != h2:
                indices += 1

        return indices