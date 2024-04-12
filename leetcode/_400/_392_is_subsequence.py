class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        if len(s) == 0:
            return True
        
        j = 0
        
        for c in t:
            if c == s[j]:
                j += 1
                if len(s) == j:
                    return True
        
        return j == len(s)
