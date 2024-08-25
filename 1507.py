class Solution:
    def reformatDate(self, date: str) -> str:
        def splitIntoTokens(date: str) -> list[str]:
            return date.split(" ")

        def formatMonth(token: str) -> str:
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            for i, month in enumerate(months):
                if token == month:
                    month_index = str(i + 1)  # since months 1 based index

            if len(month_index) == 1:  # add leading zero
                month_index = "0" + month_index
            return month_index

        def formatDay(token: str) -> str:
            day = date[0][:-2]  # strip last 2 characters (st, nd, rd, th)
            if len(day) == 1:  # add leading zero
                day = "0" + day
            return day

        def formatDateString(day: str, month: str, year: str) -> str:
            return year + "-" + month + "-" + day

        date = splitIntoTokens(date)
        day = formatDay(date[0])
        month = formatMonth(date[1])
        year = date[2]
        return formatDateString(day, month, year)