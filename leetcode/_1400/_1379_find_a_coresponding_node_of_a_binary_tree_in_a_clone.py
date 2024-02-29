from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        res = TreeNode(0)
        # DFS Solution
        def dfs(node, target):
            nonlocal res
            
            if node.val == target.val:
                res = node
                return
            
            if node.left:
                dfs(node.left, target)
            
            if node.right:
                dfs(node.right, target)

        dfs(cloned, target)
        return res

    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        head = cloned
        # BFS Solution
        
        q = deque([head])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.val == target.val:
                    return node
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
        