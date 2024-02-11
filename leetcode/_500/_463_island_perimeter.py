from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            # base case. If we reach the boundaries or if the position is water, return 1 to update parameter
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1

            if (i, j) in visit:
                return 0

            # recursion in all 4 direction
            visit.add((i, j))
            perim = dfs(i, j+1)
            perim += dfs(i+1, j)
            perim += dfs(i, j-1)
            perim += dfs(i-1, j)

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

## TODO: Add queue implementation to this problem