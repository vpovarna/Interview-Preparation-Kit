from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = 1
        ans = 0
        
        while right < len(nums):
            product *= nums[right]
            right += 1
            while left < right and product >= k:
                product = product / nums[left]
                left += 1
            ans += right - left
        
        return ans


if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 1, 1], 100))
