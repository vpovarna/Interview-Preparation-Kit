from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_count = Counter(nums)
        number_of_pairs = 0
        
        number_of_pairs = sum([int(v/2) for v in num_count.values() if v > 1])

        # Equivalent code:
            # for v in num_count.values():
            #     if v > 1:
            #         number_of_pairs += int(v/2)

        leftovers = sum(num_count.values()) - number_of_pairs * 2
        return [number_of_pairs, leftovers]



if __name__ == '__main__':
    print(Solution().numberOfPairs([1, 3, 2, 1, 3, 2, 2, 3, 3]))
    print(Solution().numberOfPairs([1, 2, 3, 4, 5]))
    print(Solution().numberOfPairs([0]))
