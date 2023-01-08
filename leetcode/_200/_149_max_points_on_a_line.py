import collections
from math import gcd, inf
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        best = 0
        for i, p1 in enumerate(points):
            slopes = collections.defaultdict(int)

            for p2 in points[i + 1:]:
                slope = self.find_slope(p1, p2)
                slopes[slope] += 1

                best = max(slopes[slope], best)

        return best + 1

    def find_slope(self, p1: List[int], p2: List[int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        if x1 - x2 == 0:
            return inf
        return (y1 - y2) / (x1 - x2)


if __name__ == '__main__':
    print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
