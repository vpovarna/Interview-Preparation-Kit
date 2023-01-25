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


if __name__ == '__main__':
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(Solution().insert([[1, 5]], [2, 3]))
