# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def traverse(node: Optional[TreeNode]):
            if node:
                traverse(node.left)
                traverse(node.right)
                ans.append(node.val)
        
        traverse(root)
        
        return ans