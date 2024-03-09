from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l < h:
            mid = (l + h) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if mid % 2 == 0:
                    h = mid - 1
                else:
                    l = mid + 1

        return nums[l]
