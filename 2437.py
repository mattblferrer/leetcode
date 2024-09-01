class Solution:
    def countTime(self, time: str) -> int:
        def getHourMinute(time: str) -> tuple[int, int]:
            hour, minute = int(time[0:2]), int(time[3:5])
            return hour, minute

        def isValidTime(hour: int, minute: int) -> bool:
            return hour < 24 and minute < 60

        def generateTimes(time: str) -> list[str]:
            valid_times = []

            for i, c in enumerate(time): # check if any ? needs to be replaced
                if c == "?":
                    q_mark = i
                    break
            else:  # if no ? encountered
                hour, minute = getHourMinute(time)
                if isValidTime(hour, minute):
                    return [time]
                return []

            # if ? encountered
            for i in range(0, 10):
                new_time = time[:q_mark] + str(i) + time[q_mark + 1:]
                valid_times += generateTimes(new_time)

            return valid_times

        return len(generateTimes(time))