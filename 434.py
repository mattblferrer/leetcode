class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        is_segment = False  # if the last character was part of a segment
        for letter in s:
            if letter != " ":
                is_segment = True  # continue segment
            else:
                if is_segment:  # only add if the space ended a segment
                    is_segment = False
                    segments += 1

        return segments + is_segment  # count segment if not ended by space