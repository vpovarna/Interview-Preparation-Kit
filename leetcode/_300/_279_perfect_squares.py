class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range (1, n +1):
            dp[i] = i
            j = 1
            while j * j <=i:
                dp[i] = min(dp[i], dp[i- j*j] + 1)
                j +=1

        return dp[n]


if __name__ == '__main__':
    print(Solution().numSquares(12))
