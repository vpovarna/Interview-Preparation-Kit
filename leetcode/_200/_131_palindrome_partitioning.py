class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def dfs(i: int, cur: list[str]):
            if i == len(s):
                res.append(cur)
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    a = cur.copy()
                    a.append(s[i: j+1])
                    dfs(j + 1, a)
        dfs(0, [])
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True