from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        new_intervals = []
        intervals.sort(key=lambda x: x[0])
        
        new_intervals.append(intervals[0])
        
        for interval in intervals[1:]:
            if  interval[0] <= new_intervals[-1][1]:
                new_intervals[-1] = [min(interval[0], new_intervals[-1][0]), max(interval[1], new_intervals[-1][1])]
            else:
                new_intervals.append(interval)
        
        return new_intervals
    
if __name__ == "__main__":
    print(Solution().merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))
    print(Solution().merge(intervals=[[1,4],[4,5]]))
