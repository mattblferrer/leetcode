class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        # get time difference between releaseTimes[i] and releaseTimes[i - 1]
        differences = [b - a for a, b in zip(releaseTimes, releaseTimes[1:])]
        differences.insert(0, releaseTimes[0])  # add 0th keypress

        max_time = 0
        for i, d in enumerate(differences):
            if d > max_time:  # new longest key press
                max_time = d
                slowest_key = keysPressed[i]
            if d == max_time:  # same duration as previous longest key press
                if slowest_key < keysPressed[i]:
                    slowest_key = keysPressed[i]
            
        return slowest_key