class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.minheap = [-s for s in stones]
        heapq.heapify(self.minheap)
        while len(self.minheap) > 1:
            x = heapq.heappop(self.minheap)
            y = heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, -abs(x - y))
        return -self.minheap[0] if self.minheap else 0

        