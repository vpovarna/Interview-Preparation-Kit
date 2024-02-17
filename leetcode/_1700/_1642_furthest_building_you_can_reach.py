import heapq
from typing import List

# 1642. Furthest Building You Can Reach
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # max heap of bricks

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff < 0:
                continue

            # update bricks value
            bricks -= diff
            # update the heap
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i

                ladders -= 1
                # - sign is to put since there is no max heap in python and we keep the values in reverse order
                bricks += -heapq.heappop(heap)

        return len(heights) - 1


if __name__ == '__main__':
    print(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
