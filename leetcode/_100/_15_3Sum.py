from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, v in enumerate(nums):
            self.twoSum(nums[i + 1:], -v, ans)
        return list(ans)


    def twoSum(self, nums, target, ans):
        visited = set()
        for n in nums:
            if target - n in visited:
                ans.add((n, target - n, -target))
            visited.add(n)


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
