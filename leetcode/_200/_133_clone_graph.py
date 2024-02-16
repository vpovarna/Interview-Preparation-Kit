import collections
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewMap = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in oldToNewMap:
                return oldToNewMap[node]

            copy = Node(node.val)
            oldToNewMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None

    def cloneGraphQueue(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        visited = {node: Node(node.val)}
        stack = [node]

        while len(stack) > 0:
            current_node = stack.pop()
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                visited[current_node].neighbors.append(visited[neighbor])
        return visited[node]
