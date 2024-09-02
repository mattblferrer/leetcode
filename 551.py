class Solution:
    def checkRecord(self, s: str) -> bool:
        consecutive_late = 0
        absents = 0

        for letter in s:
            if letter == 'A':  # absent
                consecutive_late = 0
                absents += 1
                if absents >= 2:
                    return False

            elif letter == 'L':  # late
                consecutive_late += 1
                if consecutive_late >= 3:
                    return False

            else:  # present
                consecutive_late = 0

        return True