from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(x: int, y: int, moveRemaining: int) -> int:
            if moveRemaining < 0:
                return 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1

            u = dfs(x, y + 1, moveRemaining - 1)
            d = dfs(x, y - 1, moveRemaining - 1)
            r = dfs(x + 1, y, moveRemaining - 1)
            l = dfs(x - 1, y, moveRemaining - 1)

            return l + r + d + u

        return dfs(startRow, startColumn, maxMove) % 1000000007
