from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        while self.requests:
            if t - self.requests[0] <= 3000:  # scan requests in past 3000 ms
                break
            self.requests.popleft()

        self.requests.append(t)  # add newest ping
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)