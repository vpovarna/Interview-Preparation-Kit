class BST:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findClosestValueInBst(tree: BST, target: int) -> int:
    def find_recursively(node: BST, closest):
        if node is None:
            return closest

        if abs(target - node.value) < abs(target - closest):
            closest = node.value

        if target > node.value:
            return find_recursively(node.right, closest)
        elif target < node.value:
            return find_recursively(node.left, closest)
        else:
            return closest

    return find_recursively(tree, float('inf'))


if __name__ == '__main__':
    tree = BST(10,
               BST(5,
                   BST(2, BST(1), None),
                   BST(5)),
               BST(15,
                   BST(13, None, BST(14)),
                   BST(22)
                   )
               )
    print(findClosestValueInBst(tree, 12))
