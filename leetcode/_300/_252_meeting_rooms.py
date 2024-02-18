from typing import List


class Interval(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    def __repr__(self) -> str:
        return f"({self.start},{self.end})"


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range (1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True


if __name__ == '__main__':
    print(Solution().can_attend_meetings([Interval(0,4), Interval(5,10), Interval(15, 20)]))        
