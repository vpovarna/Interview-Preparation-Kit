class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        arr = [0, 1]
        for i in range(1, n + 1):
            prev = arr[i - 1]
            cur = arr[i]
            arr.append(prev + cur)

        return arr[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(3))
