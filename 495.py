class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        time_poisoned = 0
        previous_time = -1000000000  # infinity

        # loop through times in timeSeries and subtract poison reset time
        for time in timeSeries:
            overlap = duration - time + previous_time  # poison reset time
            if overlap > 0:
                time_poisoned += duration - overlap
            else:
                time_poisoned += duration
            previous_time = time

        return time_poisoned
    