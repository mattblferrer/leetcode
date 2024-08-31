class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time_taken = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    time_taken += 1
                if tickets[k] == 0:
                    break

        return time_taken