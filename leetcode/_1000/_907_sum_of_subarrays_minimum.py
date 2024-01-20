from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0

        stack = []  # (index, num)

        for i, n in enumerate(arr):
            while len(stack) > 0 and n < stack[-1][1]:
                j, m = stack.pop()
                # count sub arrays in each size
                left = j - stack[-1][0] if len(stack) > 0 else j + 1
                right = i - j

                res = (res + m * left * right) % MOD

            stack.append((i, n))

        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n * left * right) % MOD

        return res


if __name__ == '__main__':
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))
