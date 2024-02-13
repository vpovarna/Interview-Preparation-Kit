import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrence = collections.defaultdict(int)

        for n in nums:
            occurrence[n] += 1

        max_value = max(occurrence.values())
        numbers = [k for k, v in occurrence.items() if v == max_value]
        return numbers[0] if len(numbers) > 0 else -1

if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
