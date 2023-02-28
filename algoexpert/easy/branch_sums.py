from structures import BinaryTree


def branchSums(root):
    def dfs(node: BinaryTree, curr_sum, tmp_results):
        if node is None:
            return
        curr_sum += node.value
        if not node.left and not node.right:
            tmp_results.append(curr_sum)
            return
        dfs(node.left, curr_sum, tmp_results)
        dfs(node.right, curr_sum, tmp_results)

    results = []
    dfs(root, 0, results)
    return results


if __name__ == '__main__':
    bst = BinaryTree(1,
                     BinaryTree(2,
                                BinaryTree(4,
                                           BinaryTree(8),
                                           BinaryTree(9)),
                                BinaryTree(5,
                                           BinaryTree(10),
                                           None)),
                     BinaryTree(3,
                                BinaryTree(6),
                                BinaryTree(7)))

    print(branchSums(bst))
