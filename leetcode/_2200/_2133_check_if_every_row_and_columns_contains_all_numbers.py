from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n_sum = sum([i for i in range(1, len(matrix) + 1)])
        for row in matrix:
            if sum(set(row)) != n_sum:
                return False

        t_matrix = zip(*matrix)

        for row in t_matrix:
            if sum(set(row)) != n_sum:
                return False

        return True


if __name__ == '__main__':
    print(Solution().checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
    print(Solution().checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]))
