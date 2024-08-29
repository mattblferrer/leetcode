class Solution:
    def countPoints(self, rings: str) -> int:
        ring_colors = dict()

        for i in range(0, len(rings), 2):
            color, rod = rings[i], rings[i + 1]  # get color, rod pair
            if rod not in ring_colors:
                ring_colors[rod] = color  # store as string
            else:
                if color not in ring_colors[rod]:
                    ring_colors[rod] += color  # append to existing string
        
        rods_with_all = 0  # rods with all 3 colors of rings
        for rod, colors in ring_colors.items():
            if len(colors) == 3:
                rods_with_all += 1

        return rods_with_all