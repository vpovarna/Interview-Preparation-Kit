from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    ## BFS algorithm
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, False)])
        total_sum = 0

        while q:
            node, is_left = q.popleft()
            if is_left and not node.left and not node.right:
                total_sum += node.val
            
            if node.left:
                q.append((node.left, True))
            if node.right:
                q.append((node.right, False))

        return total_sum
    
    ## DFS Solution
    def sumOfLeftLeavesV2(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if not node:
                return 0
            
            if not node.left and not node.right:
                if is_left:
                    return node.val
                else:
                    return 0
            
            left_sum = dfs(node.left, True) # Traverse left child
            right_sum = dfs(node.right, False) # Traverse right child

            return left_sum + right_sum


        return dfs(root, False)
