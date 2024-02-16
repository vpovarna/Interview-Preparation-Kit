from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = 0
        
        for n in nums:
            if total > n:
                res = total + n
            total +=n
        
        return res
        

if __name__ == "__main__":
    print(Solution().largestPerimeter([5,5,5]))