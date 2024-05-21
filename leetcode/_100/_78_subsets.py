class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        ans = [[]]
        
        for num in nums:
            ans += [cur + [num] for cur in ans]
        return ans

if __name__ == "__main__":
    print(Solution().subsets([1,2,3]))
