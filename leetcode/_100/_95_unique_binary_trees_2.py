from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left: int, right: int):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]

            res = []
            for val in range(left, right + 1):
                for leftTree in generate(left, val - 1):
                    for rightTree in generate(val+1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)
            return res

        return generate(1, n)
