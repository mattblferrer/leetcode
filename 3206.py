class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)
        alternating = 0  # number of alternating groups

        for i in range(n):
            if colors[(i - 1) % n] != colors[i] != colors[(i + 1) % n]:
                alternating += 1

        return alternating