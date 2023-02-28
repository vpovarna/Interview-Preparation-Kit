from structures import BinaryTree


def findClosestValueInBst(tree: BinaryTree, target: int) -> int:
    def find_recursively(node: BinaryTree, closest):
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
    tree = BinaryTree(10,
               BinaryTree(5,
                   BinaryTree(2, BinaryTree(1), None),
                   BinaryTree(5)),
               BinaryTree(15,
                   BinaryTree(13, None, BinaryTree(14)),
                   BinaryTree(22)
                   )
               )
    print(findClosestValueInBst(tree, 12))
