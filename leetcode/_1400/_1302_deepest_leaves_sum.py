# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = deque([root])
        ans = 0
        
        ## BFS does a level order traversal so, we care computing the sum for all depths and we return the last one which in this case will be the longest path.
        while q:
            size = len(q)
            current_sum  = 0 
            for _ in range(size):
                current_node = q.popleft()
                current_sum += current_node.val
                
                if current_node.left is not None:
                    q.append(current_node.left)
                    
                if current_node.right is not None:
                    q.append(current_node.right)
                
            ans = current_sum
        
        return ans
        
        