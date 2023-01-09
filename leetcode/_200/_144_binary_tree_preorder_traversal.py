from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: TreeNode) -> List[int]:
            if node is None:
                return result

            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return result

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal2(root.left) + self.preorderTraversal2(root.right)

    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]

        while stack:
            temp = stack.pop()

            if temp:
                ans.append(temp.val)
                stack.append(temp.left)
                stack.append(temp.right)

        return ans
