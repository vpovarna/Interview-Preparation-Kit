from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        left_most_node = None
        # BFS Solution
        while queue:
            left_most_node = queue.popleft()
            if left_most_node.right:
                queue.append(left_most_node.right)
            if left_most_node.left:
                queue.append(left_most_node.left)
        
        return left_most_node.val
    
    def findBottomLeftValueV2(self, root: Optional[TreeNode]) -> int:        
        ans = [0]
        max_depth = [0]
        curr_depth = 1
        
        #DFS Solution
        def dfs(root, curr_depth):
            if not root:
                return
            
            if curr_depth > max_depth[0]:
                ans[0] = root.val
                max_depth[0] = curr_depth
            dfs(root.left, curr_depth + 1)
            dfs(root.right, curr_depth + 1)
        
        dfs(root, curr_depth)
        return ans[0]    

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    print(Solution().findBottomLeftValue(root))
