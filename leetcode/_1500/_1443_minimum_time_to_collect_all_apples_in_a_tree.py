from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], has_apple: List[bool]) -> int:
        parents = [-1] * n
        for edge in edges:
            parent, child = edge
            if parents[child] == -1:
                parents[child] = parent
            else:
                parents[parent] = child
        for h in range(n - 1, 0, -1):
            if has_apple[h] and parents[h] != -1:
                has_apple[parents[h]] = True

        return sum(has_apple[1:]) * 2


if __name__ == '__main__':
    print(Solution()
          .minTime(n=7,
                   edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                   has_apple=[False, False, True, False, True, True, False]
                   )
          )
