import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        class Worker:  # for easier comparison in min-heap
            def __init__(self, time):
                self.total_time = 0
                self.time = time
                self.height = 1  # height reduced by worker

            def __lt__(self, other):  # compare total time after worker job
                self_val = self.total_time + self.time * self.height
                other_val = other.total_time + other.time * other.height
                return self_val < other_val

        workerTimes.sort()
        min_workers = [Worker(time) for time in workerTimes]
        heapq.heapify(min_workers)  # priority queue of workers

        while mountainHeight > 0:  # get worker with minimum time after job
            next_worker = heapq.heappop(min_workers)
            next_worker.total_time += next_worker.time * next_worker.height
            next_worker.height += 1  # increase height worker worked on
            heapq.heappush(min_workers, next_worker)
            mountainHeight -= 1

        max_time = 0
        for worker in min_workers:  # get maximum time spent by any worker
            max_time = max(worker.total_time, max_time)

        return max_time