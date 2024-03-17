from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        for i, (x, y) in enumerate(intervals):
            if y < new_interval[0]:
                result.append([x, y])
            elif new_interval[1] < x:
                i -= 1
                break
            else:
                new_interval[0] = min(new_interval[0], x)
                new_interval[1] = max(new_interval[1], y)

        return result + [new_interval] + intervals[i + 1:]

    def insertV2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged


if __name__ == '__main__':
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(Solution().insert([[1, 5]], [2, 3]))
