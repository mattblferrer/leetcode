class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        def timeToMins(time: str) -> int:
            hh, mm = int(time[0:2]), int(time[3:5])
            return hh * 60 + mm

        a1, a2 = timeToMins(event1[0]), timeToMins(event1[1])
        b1, b2 = timeToMins(event2[0]), timeToMins(event2[1])

        return a2 >= b1 and not (a1 > b2)