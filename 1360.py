class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def getYearMonthDay(date: str) -> tuple[int, int, int]:
            year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
            return year, month, day

        def leapYearsSince(year: int) -> int:
            leap_years = 0
            for y in range(1968, year + 1):
                leap_years += isLeapYear(y)
            return leap_years

        def isLeapYear(year: int) -> bool:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return year % 4 == 0
            
        def daysSinceStart(year: int, month: int, day: int) -> int:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if isLeapYear(year) and month < 3:  # leap day check
                total_days = (year - 1968) * 365 + leapYearsSince(year) - 1
            else:
                total_days = (year - 1968) * 365 + leapYearsSince(year)
            total_days += sum(month_days[:month - 1]) + day  # for month, day
            return total_days

        y1, m1, d1 = getYearMonthDay(date1)
        y2, m2, d2 = getYearMonthDay(date2)
        return abs(daysSinceStart(y1, m1, d1) - daysSinceStart(y2, m2, d2))