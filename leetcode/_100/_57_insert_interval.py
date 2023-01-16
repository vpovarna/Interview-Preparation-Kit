from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                result.append([x, y])
            elif newInterval[1] < x:
                i -= 1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)

        return result + [newInterval] + intervals[i + 1:]


if __name__ == '__main__':
    # print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    # print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(Solution().insert([[1, 5]], [2, 3]))
