from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count_digits = Counter(nums)
        return sorted(nums, key = lambda x: (count_digits[x], -x))  # this replace matrix inversion and array concatenation after sort


if __name__ == '__main__':
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
    print(Solution().frequencySort([2, 3, 1, 3, 2]))
