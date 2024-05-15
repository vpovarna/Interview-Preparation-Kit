from collections import deque
import heapq

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        distance_matrix = self.get_distances_matrix(grid)
        n = len(distance_matrix)
        
        h = [(-distance_matrix[0][0], 0, 0)]
        visited = set([(0,0)])
        
        res = float('inf')
        
        while h: 
            d, row, col = heapq.heappop(h)
            res = min(res, -d)
            if row == n - 1 and col == n - 1:
                return res
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if 0 <= new_row < n and 0 <= new_col < n:
                    if (new_row, new_col) in visited:
                        continue
                    heapq.heappush(h, (-distance_matrix[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col)) 
            
        return -1
    
    def get_ones_locations(self, grid:list[list[int]]) -> set[(int, int)]:
        ones = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones.add((i, j))
        return ones
    
    def get_distances_matrix(self, grid:list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ones = self.get_ones_locations(grid)
        distance_matrix = [ [float('inf')] * n   for _ in range(n)]
        
        # calculate manhattan distance from the once points
        for x, y in ones:
            q = deque([(x, y, 0)])
            seen = set()
            
            while q:
                row, col, d = q.popleft()
                if (row, col) in seen:
                    continue
                
                seen.add((row, col))
                if d >= distance_matrix[row][col]:
                    continue
                
                distance_matrix[row][col] = d
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < n and 0 <= new_col < n:
                        q.append((new_row, new_col, d + 1))
            
        return distance_matrix
        

if __name__ == "__main__":
    input_grid = [[1,0,0],[0,0,0],[0,0,1]]
    # print(Solution().get_distances_matrix(input_grid))
    print(Solution().maximumSafenessFactor(grid=input_grid))
