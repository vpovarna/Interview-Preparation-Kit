import collections
from typing import List


# 1481 - Least Number of Unique Integers after K Removals
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map = collections.defaultdict(int)
        for n in arr:
            map[n] += 1

        sorted_values = sorted(list(map.values()))
        print(sorted_values)

        sorted_values_length = len(sorted_values)
        for n in sorted_values:
            if n <= k:
                sorted_values_length -= 1
                k -= n

        return sorted_values_length


if __name__ == '__main__':
    print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
    print(Solution().findLeastNumOfUniqueInts([1, 1, 2, 2, 3, 3], 3))
