import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap_nums = heapq.heapify(nums)
        for i in range(len(nums) - k):  # pop n-k smallest elements
            heapq.heappop(nums)
        return heapq.heappop(nums)