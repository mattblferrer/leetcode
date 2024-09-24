class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        start_segment = False
        end_segment = False

        for bit in s:
            if bit == '1':
                start_segment = True
            if start_segment and bit == '0':
                end_segment = True
            if end_segment and bit == '1':
                return False

        return True