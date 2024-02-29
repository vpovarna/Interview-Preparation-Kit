class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, grandParentIsEven, parentIsEven):
            nonlocal result
            if node is None:
                return

            if grandParentIsEven:
                result += node.val

            dfs(node.left, parentIsEven, node.val % 2 == 0)
            dfs(node.right, parentIsEven, node.val % 2 == 0)

        dfs(root, False, False)
        return result
