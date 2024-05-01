from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        def traverse(node: Optional[TreeNode], depth_left: int) -> None:
            if node is None:
                return

            if depth_left == 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val, left=old_left)
                node.right = TreeNode(val, right=old_right)

                return

            traverse(node.left, depth_left - 1)
            traverse(node.right, depth_left - 1)

        traverse(root, depth - 1)
        return root
