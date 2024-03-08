from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for n in nums:
            dict[n] +=1
            
        max_value = max(dict.values())
        
        return sum([n for n in dict.values() if n == max_value])
            
if __name__ == '__main__':
    print(Solution().maxFrequencyElements([1,2,2,3,1,4]))
    print(Solution().maxFrequencyElements([1,2,3,4,5]))