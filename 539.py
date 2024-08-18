class Solution:
    def convertToMinutes(self, time: str) -> int:
        hours, mins = int(time[0:2]), int(time[3:5])
        return hours * 60 + mins

    def findMinDifference(self, timePoints: list[str]) -> int:
        # convert array to number of minutes for easier comparison
        times = sorted([self.convertToMinutes(time) for time in timePoints])
        times.append(min(times))  # for diff between last and first element
        time_differences = [min(abs(b - a), 1440 - abs(b - a)) for a, b in 
            zip(times, times[1:])]  # account for forward, backward time

        return min(time_differences)