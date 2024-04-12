from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)
        for i in range(n):
            res[i] = nums[i]
            res[i + n] = nums[i]

        return res


if __name__ == "__main__":
    print(Solution().getConcatenation(nums=[1, 2, 1]))
