# Definition for a Node.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = dict()
        def dfs(old_node):
            if old_node in old_to_new:
                return old_to_new[old_node]

            new_node = Node(old_node.val)
            old_to_new[old_node] = new_node
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node) if node else None
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors.extend([node2, node4])
node2.neighbors.extend([node1, node3])
node3.neighbors.extend([node2, node4])
node4.neighbors.extend([node1, node3])
s = Solution().cloneGraph(node1)
print(node1, s)
