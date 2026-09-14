class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math 
        minHeap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(minHeap,(dist,point))

        result = []
        for i in range(k):
            dist, point = heapq.heappop(minHeap)
            result.append(point)
        return result


        