from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + int((r - l) / 2)

            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

if __name__ == '__main__':
    print(Solution().search(nums = [-1,0,3,5,9,12], target = 9))
    print(Solution().search(nums = [-1,0,3,5,9,12], target = 2))

