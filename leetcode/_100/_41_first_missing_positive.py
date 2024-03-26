from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in unique_nums:
                return i

        return len(nums) + 1

    def first_missing_positive_v2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            ind = abs(nums[i]) - 1
            if ind < 0 or ind >= n:
                continue

            if nums[ind] > 0:
                nums[ind] *= -1
            elif nums[ind] == 0:
                nums[ind] = float('-inf')

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n


if __name__ == "__main__":
    # print(Solution().first_missing_positive_v2([1, 2, 0]))
    print(Solution().first_missing_positive_v2([3, 4, -1, 1]))
    # print(Solution().first_missing_positive_v2([7, 8, 9, 11, 12]))
