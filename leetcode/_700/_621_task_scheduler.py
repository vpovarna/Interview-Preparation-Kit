from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        
        # run this as long as there are values in the heap and in the queue
        while maxHeap or q:
            time += 1

            if maxHeap:
                # get the latest value from the heep and added to queue, after you decrease the value by 1 and update the time
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            # if the first value time is equal to the current time, remove the value and add it to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time