
class Solution:
    def dayOfYear(self, date: str) -> int:
        def isLeapYear(year: int) -> bool:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return year % 4 == 0

        def extractYearMonthDay(date: str) -> tuple[int, int, int]:
            year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
            return year, month, day

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date_data = extractYearMonthDay(date)
        year, month, day = date_data[0], date_data[1], date_data[2]
        day_number = sum(month_days[:month - 1]) + day  # without leap years

        if isLeapYear(year) and day_number >= 60:  # consider leap years
            if month >= 3:  # YYYY-03-01 and beyond
                return day_number + 1
        return day_number
    