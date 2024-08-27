class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested = 0
        for i, b in enumerate(batteryPercentages):
            if b == 0:  # move to next device without testing
                continue
            tested += 1
            for j in range(i + 1, len(batteryPercentages)):  # decrease battery
                batteryPercentages[j] = max(0, batteryPercentages[j] - 1)

        return tested