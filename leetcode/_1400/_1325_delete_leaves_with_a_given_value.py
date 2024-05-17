from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right and root.val == target:
            return None
        else:
            return root
        
    # iterative solution        
    def removeLeafNodesV2(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visit = set()
        parents = {root: None}
        
        while stack:
            node = stack.pop()
            # if it's a leaf node
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    # Check if it's the parent
                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visit:
                visit.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        return root
