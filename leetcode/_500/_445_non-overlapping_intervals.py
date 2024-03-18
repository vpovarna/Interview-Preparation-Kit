from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort()
        ans  = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # update the prevEnd to the new end value and move fw
                prevEnd = end
            else:
                # increase the counter and keep the interval with the minimum end value
                ans +=1
                prevEnd = min(end, prevEnd)
        
        return ans
    

if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals(intervals=[[1,2],[2,3],[3,4],[1,3]]))
    print(Solution().eraseOverlapIntervals(intervals=[[1,2],[1,2],[1,2]]))
    print(Solution().eraseOverlapIntervals(intervals=[[1,2],[2,3]]))
    print(Solution().eraseOverlapIntervals(intervals=[[1,100],[11,22],[1,11],[2,12]]))
