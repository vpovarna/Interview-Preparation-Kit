from typing import List


class Interval(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    def __repr__(self) -> str:
        return f"({self.start},{self.end})"


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        res, count = 0, 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count +=1
                s+=1
            else:
                count -=1
                e +=1
            res = max(res, count)
        return res

if __name__ == '__main__':
    print(Solution().minMeetingRooms([Interval(0,30), Interval(5, 10), Interval(15, 20)]))
