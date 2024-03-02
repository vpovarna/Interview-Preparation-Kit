from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative_numbers = deque()
        positive_numbers = deque()
        
        for n in nums:
            if n < 0:
                negative_numbers.append(n * n)
            else:
                positive_numbers.append(n * n)
                
                
        ans = []
        while len(negative_numbers) > 0 and len(positive_numbers) > 0:
            if negative_numbers[-1] > positive_numbers[0]:
                ans.append(positive_numbers.popleft())
            else:
                ans.append(negative_numbers.pop())

        while negative_numbers:
            ans.append(negative_numbers.pop())
        
        while positive_numbers:
            ans.append(positive_numbers.popleft())

        return ans

if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
