class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        
        def dfs(i: int, total: int) -> int:
            #base case
            if i == len(nums):
                return total
            
            v1 = dfs(i + 1, total ^ nums[i]) # include nums[i]
            v2 = dfs(i + 1, total) # not include nums[i]
            return v1 + v2
        
        return dfs(0, 0)