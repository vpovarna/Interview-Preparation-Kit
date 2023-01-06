from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp1 = [1] * len(nums)
        for i in range(1, len(nums)):
            dp1[i] = (nums[i - 1] * dp1[i - 1])

        dp2 = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            dp2[i] = (dp2[i + 1] * nums[i + 1])

        return [dp1[i] * dp2[i] for i in range(len(dp1))]


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
