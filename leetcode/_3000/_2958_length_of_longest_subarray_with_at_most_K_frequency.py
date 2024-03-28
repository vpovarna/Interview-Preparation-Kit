from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        right = 0

        dict = defaultdict(int)

        while right < len(nums):
            current_num = nums[right]
            dict[current_num] += 1
            
            while dict[current_num] > k:
                dict[nums[left]] -= 1
                left += 1


            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


if __name__ == "__main__":
    print(Solution().maxSubarrayLength(nums=[2,2,3], k=1))
    print(Solution().maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
    print(Solution().maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
    print(Solution().maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
