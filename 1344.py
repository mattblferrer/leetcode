class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_deg = minutes * 6
        hour_deg = (hour % 12) * 30 + minutes * 0.5
        angle = abs(hour_deg - minute_deg)  # can be bigger or smaller angle

        return min(angle, 360 - angle)  # return smaller angle