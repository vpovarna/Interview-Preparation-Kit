from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left =None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Left -> Root -> Right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        
        def dfs(node: Optional[TreeNode]):
            if node is not None:
                dfs(node.left)
                values.append(node.val)
                dfs(node.right)
        
        dfs(root)
        
        return values
    
    def inorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        
        node = root
        stack = []
        
        while node or len(stack) > 0:
            if node:
                stack.append(node)
                node = node.left
            else:
                current_node = stack.pop()
                values.append(current_node.val)
                node = current_node.right

  
        return values

if __name__ == '__main__':
    node = TreeNode(val= 1, right = TreeNode(2, left=TreeNode(3)))
    print(Solution().inorderTraversalStack(node))
    