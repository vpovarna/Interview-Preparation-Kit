from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        max_count = 0
        max_value = max(nums)
        ans = 0
        
        for right in range(len(nums)):
            if nums[right] == max_value:
                max_count += 1
        
            while max_count > k or (left <= right and max_count == k and nums[left] != max_value):
                if nums[left] == max_value:
                    max_count -= 1
                left +=1
            
            if max_count == k:
                ans += left + 1
        return ans
