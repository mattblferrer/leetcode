class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        days = 0
        for i in range(len(hours) - 1):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    days += 1

        return days