from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, cur):
            if not node:
                return
            
            cur = chr(ord('a') + node.val) + cur
            
            if node.left and node.right:
                return min(
                    dfs(node.left, cur),
                    dfs(node.right, cur)
                )

            if node.right:
                return dfs(node.right, cur)                
            if node.left:
                return dfs(node.left, cur)
                
            return cur

        return dfs(root, "")
            