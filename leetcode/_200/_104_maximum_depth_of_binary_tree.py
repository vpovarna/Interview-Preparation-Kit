class TreeNode(object):
    def __init__(self, value, left, right) -> None:
        self.value = value
        self.left = left
        self.right = right

class Solution(object):

    #DFS recursive on left subtree and on the right subtree
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
