from structures import BinaryTree


def nodeDepths(node, depth=0):
    # Write your code here.
    if node is None:
        return 0
    else:
        return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)


if __name__ == '__main__':
    tree = BinaryTree(1,
                      BinaryTree(2,
                                 BinaryTree(4, BinaryTree(8), BinaryTree(9)),
                                 BinaryTree(5)),
                      BinaryTree(3,
                                 BinaryTree(6), BinaryTree(7)
                                 )
                      )

    print(nodeDepths(tree))
