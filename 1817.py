class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        uam = dict()
        for id_i, time in logs:  # log all unique minutes in set for each id
            if id_i not in uam:
                uam[id_i] = set([time])
            else:
                uam[id_i].add(time)
        
        answer = [0] * k
        for id_i, times in uam.items():
            answer[len(times) - 1] += 1  # since 1-indexed
        return answer