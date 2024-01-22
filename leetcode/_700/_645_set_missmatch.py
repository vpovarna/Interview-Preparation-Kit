from typing import List
from collections import defaultdict


class Solution(object):
    def findErrorNums(self, nums) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        dic = defaultdict(int)
        for i, n in enumerate(nums):
            dic[n] += 1

        for k, v in dic.items():
            if v > 1:
                ans.append(k)

        numSet = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in numSet:
                ans.append(n)

        return ans

    # math solution
    def findErrorNums(self, nums) -> List[int]:
        duplicate_num = sum(nums) - sum(set(nums))
        expected_sum = sum(range(1, len(nums) + 1))
        actual_sum = sum(set(nums))

        missing_num = expected_sum - actual_sum
        return [duplicate_num, missing_num]


if __name__ == '__main__':
    print(Solution().findErrorNums([1, 2, 2, 4]))
