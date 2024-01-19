class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        N = len(matrix)

        cache = {}

        def dfs(r, c):
            # reach the end of the matrix
            if r == N:
                return 0

            # negate this possibility by returning a very large number
            if c < 0 or c == N:
                return float("inf")

            if (r, c) in cache:
                return cache[(r, c)]

            res = matrix[r][c] + min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c + 1),
                dfs(r + 1, c)
            )
            cache[(r, c)] = res

            return res

        ans = float("inf")
        for c in range(N):
            # we can start from any column from the first row
            ans = min(ans, dfs(0, c))

        return ans

    def minFallingPathSumButtomUP(self, matrix):
        N = len(matrix)
        for r in range (1, N):
            for c in range(N):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c > 0 else float("inf")
                right = matrix[r-1][c+1] if c < N else float("inf")
                matrix[r][c] = matrix[r][c] + min(mid, left, right)

        # the value is in the last row, get the minimum.
        return min(matrix[-1])


if __name__ == '__main__':
    problem = Solution()
    matrix = [
        [2, 1, 3],
        [6, 5, 7],
        [7, 8, 9]
    ]

    print(problem.minFallingPathSum(matrix=matrix))
