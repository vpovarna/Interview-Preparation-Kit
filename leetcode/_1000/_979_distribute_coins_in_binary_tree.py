from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res

            if not node:
                return 0

            extra_coins = 0
            l_extra = dfs(node.left)
            r_extra = dfs(node.right)

            extra_coins = node.val -1 + l_extra + r_extra
            res += abs(extra_coins)
            return extra_coins

        dfs(root)
        return res
       