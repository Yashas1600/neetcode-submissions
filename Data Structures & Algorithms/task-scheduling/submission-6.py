class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        the q will be the alphabet and how waht time i t can be activated at 
        then i will maintain the time
        ill kjeep doign this while q:
        i think i also need the count of eahc alphabet if i ma not wrong 
        maybe. ahashmap for that 
        i dont even think i need to 
        keep runnign the most frequent task

        """
        from collections import Counter
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
       
        time = 0
        q = deque()


        while maxHeap or q:
            time +=1
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    q.append((freq,time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                

        


        
        