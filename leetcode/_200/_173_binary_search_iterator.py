from typing import Optional


class TreeNode:
    def __init__(self, val:int = 0, right = None, left = None) -> None:
        self.val = val
        self.right = right
        self.left = left

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node is not None:
            self.stack.append(node)
            node = node.left
        

    def next(self) -> int:
        res = self.stack.pop()
        
        current_node = res.right
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left
        
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0