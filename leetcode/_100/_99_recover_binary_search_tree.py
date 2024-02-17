from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # in order traversal using yield
        def dfs(root:Optional[TreeNode]):
            if root.left is not None:
                yield from dfs(root.left)
            
            yield root
            
            if root.right is not None:
                yield from dfs(root.right)
        
        nodes = [node for node in dfs(root)]
        sorted_value = sorted([n.val for n in nodes])
        
        # updating all nodes values
        for n, val in zip(nodes, sorted_value):
            n.val = val
            
    def recoverTreeV2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        
        # in order traversal using yield
        def dfs(node:Optional[TreeNode]):
            if node is None:
                return
            
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        dfs(root)
        
        sorted_value = sorted([n.val for n in nodes])
        
        # updating all nodes values
        for n, val in zip(nodes, sorted_value):
            n.val = val

    def recoverTreeV3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        
        # in order traversal using yield
        def dfs(node:Optional[TreeNode]):
            if node is None:
                return
            
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        dfs(root)
        
        sorted_order = sorted(nodes, key=lambda x:x.val)
        for i in range(len(nodes)):
            if nodes[i] != sorted_order[i]:
                nodes[i].val, sorted_order[i].val = sorted_order[i].val, nodes[i].val
                return