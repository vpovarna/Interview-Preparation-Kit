import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        R, C = len(grid), len(grid[0])
        visited = set()

        nr_of_islands = 0

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.pop()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for r_diff, c_diff in directions:
                    r, c = row + r_diff, col + c_diff
                    # boundary checks
                    if (r >= 0 and r < R and
                        c >= 0 and c < C and
                        grid[r][c] == "1" and
                            (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    nr_of_islands += 1

        return nr_of_islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))
