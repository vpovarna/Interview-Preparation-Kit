class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        ans = 0
        i = 0
        
        while k > 0:
            max_value = max(happiness[i] - i, 0)
            ans += max_value
            i += 1
            k -= 1
                
        return ans
    
if __name__ == "__main__":
    print(Solution().maximumHappinessSum(happiness = [1,2,3], k = 2))
