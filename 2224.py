class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def timeToMinutes(time: str) -> int:
            hh, mm = int(time[0:2]), int(time[3:5])
            return hh * 60 + mm

        current = timeToMinutes(current)  # convert to minutes after 00:00
        correct = timeToMinutes(correct)
        diff = correct - current 
        operations = 0

        for time_inc in [60, 15, 5, 1]:  # pick greatest time increase (greedy)
            operations += diff // time_inc
            diff %= time_inc

        return operations