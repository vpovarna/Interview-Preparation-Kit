from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def robDP(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    print(Solution().robDP([1, 2, 3, 1]))
    print(Solution().rob([1, 2, 3, 1]))
