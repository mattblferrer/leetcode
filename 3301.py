class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
        maximumHeight = sorted(maximumHeight, reverse=True)
        actual_heights = [maximumHeight[0]]
        heights_used = set(actual_heights)

        for i, m in enumerate(maximumHeight[1:], start=1):
            h = min(m, actual_heights[i - 1])
            while True:
                if h == 0:  # no height, not possible
                    return -1
                if h in heights_used:
                    h -= 1
                else:
                    break

            actual_heights.append(h)
            heights_used.add(h)

        return sum(actual_heights)