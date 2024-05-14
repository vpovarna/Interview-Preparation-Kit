from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            cur = grid[i][j]
            grid[i][j] = 0
            local_max = cur
            
            for ii, jj in directions:
                new_i = ii + i
                new_j = jj + j
                local_max = max(local_max, cur + dfs(new_i, new_j))        

            # After we compute the local_max we had to reset the grid value for i and j, to compute the path again
            grid[i][j] = cur
            return local_max
            
        max_value = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_value = max(dfs(i, j), max_value)
                    
        return max_value

if __name__ == "__main__":
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    print(Solution().getMaximumGold(grid=grid))
