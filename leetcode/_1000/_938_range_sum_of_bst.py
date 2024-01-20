from typing import Optional


class TreeNode:
    def __init__(self, val=0, left =None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def bst_traversal(subtree: Optional[TreeNode]) -> int:
            if not subtree:
                return 0
            range_value = subtree.val if low <= subtree.val <= high else 0

            return bst_traversal(subtree.left) + range_value + bst_traversal(subtree.right)

        return bst_traversal(root)


if __name__ == '__main__':
    tree = TreeNode(val=10,
                    left=TreeNode(val=5,
                                  left=TreeNode(val=3),
                                  right=TreeNode(val=7)
                                  ),
                    right=TreeNode(val=15,
                                   right=TreeNode(val=18)
                                   )
                    )

    print(Solution().rangeSumBST(tree, 7, 15))
