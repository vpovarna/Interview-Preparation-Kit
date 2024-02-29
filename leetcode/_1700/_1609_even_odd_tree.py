# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Save the current level in a boolean called even
        even = True
        queue = deque([root])
        
        while queue:
            # The current value will be checked against prev. For even level the initial value is infinity and for odd level the initial value is minus infinity
            prev = float("-inf") if even else float("inf")
            
            size = len(queue)
            for _ in range(size):
                current_node = queue.popleft()
                if even:
                    if current_node.val % 2 == 0 or current_node.val <= prev:
                        return False
                else:
                    if current_node.val % 2 == 1 or current_node.val >= prev:
                        return False 
                
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)

                prev = current_node.val
            even = not even
        
        return True
