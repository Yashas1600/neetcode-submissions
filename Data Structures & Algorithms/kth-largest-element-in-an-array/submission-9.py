class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        """
        # why do we set minHeap to [] instead of doing minHeap = nums then heapifying nums
        minHeap = []
        # need to turn into maxHeap

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
