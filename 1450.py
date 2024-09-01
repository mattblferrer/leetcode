class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        busy_students = 0  # count number of students doing homework
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                busy_students += 1

        return busy_students