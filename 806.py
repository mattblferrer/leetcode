class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        current_pixels = 0
        lines = 1
        for char in s:
            pos = ord(char) - 97  # position in the alphabet (0-indexed)
            if current_pixels + widths[pos] > 100:  # check for char overflow
                current_pixels = widths[pos]
                lines += 1
            else:
                current_pixels += widths[pos]

        return [lines, current_pixels]