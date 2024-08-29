class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        min_moves = 0
        for seat, student in zip(seats, students):
            min_moves += abs(student - seat)  # distance of student from seat
        
        return min_moves