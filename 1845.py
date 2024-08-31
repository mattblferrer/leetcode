import heapq

class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n + 1)]  # all seats unreserved
        heapq.heapify(self.unreserved)

    def reserve(self) -> int:
        reserved = heapq.heappop(self.unreserved)  # pop smallest-numbered seat
        return reserved

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)