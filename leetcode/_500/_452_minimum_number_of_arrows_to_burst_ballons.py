from typing import List


class Solution:

    # Here we need to find how many non-overlapping intervals we have.
    # Intervals [1,2] and [2,3] overlapping, because they have common end.

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sorting ascending by x_end
        points.sort(key=lambda x: x[1])
        res = 1
        last_end = points[0][1]
        # iterate and deconstruct array in one line
        for x_start, x_end in points[1:]:
            if x_start > last_end:
                res += 1
                last_end = x_end

        return res


if __name__ == '__main__':
    print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
