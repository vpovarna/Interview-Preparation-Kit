class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:

        m = len(grid)
        n = len(grid[0])

        return_grid = []

        def get_max_value(i: int, j: int) -> int:
            max_value = float('-inf')
            for ii in range(3):
                for jj in range(3):
                    max_value = max(max_value, grid[ii + i][jj + j])
            
            return max_value
        

        for i in range(m - 2):
            row = []
            for j in range(n - 2):
                max_value = get_max_value(i, j)
                row.append(max_value)
            return_grid.append(row)

        return return_grid
    

if __name__ == "__main__":
    # grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    # print(Solution().largestLocal(grid))

    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(Solution().largestLocal(grid))

