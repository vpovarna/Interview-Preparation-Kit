from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            dic[node.val] += 1
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            count = 0
            if not node.left and not node.right:
                count = 1 if ispseudopath(dic) else 0
            dic[node.val] -= 1

            return left_count + right_count + count

        def ispseudopath(dic: dict) -> bool:
            count = 0
            for key in dic:
                if dic[key] % 2 > 0:
                    count += 1
            return count == 1 or count == 0

        return dfs(root)
