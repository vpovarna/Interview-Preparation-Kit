from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        return sum(range(size + 1)) - sum(nums)


if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0, 1]))
