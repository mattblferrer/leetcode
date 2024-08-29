class Solution:
    def minimumChairs(self, s: str) -> int:
        minimum_chairs = 0
        people = 0
        for event in s:
            if event == 'E':  # enters the waiting room
                people += 1
            else:  # leaves the waiting room
                people -= 1
            minimum_chairs = max(minimum_chairs, people)

        return minimum_chairs