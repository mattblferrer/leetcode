class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def extractMonthDay(date: str) -> tuple[int, int]:
            month, day = int(date[:2]), int(date[3:5])
            return month, day

        def convertToDayNumber(month: int, day: int) -> int:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(month_days[:month - 1]) + day

        # extract day and month information
        aa_data = extractMonthDay(arriveAlice)
        la_data = extractMonthDay(leaveAlice)
        ab_data = extractMonthDay(arriveBob)
        lb_data = extractMonthDay(leaveBob)

        # convert to day number
        aa_day = convertToDayNumber(aa_data[0], aa_data[1])
        la_day = convertToDayNumber(la_data[0], la_data[1])
        ab_day = convertToDayNumber(ab_data[0], ab_data[1])
        lb_day = convertToDayNumber(lb_data[0], lb_data[1])

        # calculate days spent together
        return max(min(la_day, lb_day) - max(aa_day, ab_day) + 1, 0)