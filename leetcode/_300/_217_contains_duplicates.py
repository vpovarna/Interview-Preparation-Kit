from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            else:
                visited.add(n)
        return False
