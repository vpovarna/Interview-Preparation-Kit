from typing import List
from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = defaultdict(int)
        
        for n in nums:
            visited[n] += 1
        
        return [key for (key, value) in visited.items() if value > 1]

    def findDuplicatesV2(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if (nums[abs(n) - 1] < 0):
                ans.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        
        return ans        

if __name__ == "__main__":
    print(Solution().findDuplicatesV2([1,1,2,2]))
