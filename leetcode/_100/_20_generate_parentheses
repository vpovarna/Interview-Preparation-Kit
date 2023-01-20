from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        ans = []
        self.dfs("", ans, n, n)
        return ans

    def dfs(self, substring: str, ans: List[str], left: int, right: int):
        if left > right:
            return

        if left == 0 and right == 0:
            ans.append(substring)
            return

        if left > 0:
            self.dfs(substring + "(", ans, left - 1, right)

        if right > 0:
            self.dfs(substring + ")", ans, left, right - 1)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
