import collections
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        f = collections.Counter()
        f[0] = 1
        
        prefix = [0]
        count = 0
        
        for x in nums:
            last = prefix[-1] + x
            prefix.append(last)
            
            ## add to the counter how many times we seen the last value - goal
            count += f[last - goal]
            f[last] += 1
            
        return count
