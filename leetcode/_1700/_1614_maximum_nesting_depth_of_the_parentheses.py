class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            elif s[i] == ")":
                depth -= 1
            maxi = max(maxi, depth)
        return maxi
        