from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (o(N) time complexity)
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_tree_balanced = self.is_balanced(root.left) and self.is_balanced(root.right)

        l = self.calculate_max_depth(root.left)
        r = self.calculate_max_depth(root.right)

        return (abs(l - r) <= 1) and is_tree_balanced

    # dfs solution

    def calculate_max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_binary_tree_depth = self.calculate_max_depth(root.left)
        right_binary_tree_depth = self.calculate_max_depth(root.right)

        return max(left_binary_tree_depth, right_binary_tree_depth) + 1


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().is_balanced(root))
