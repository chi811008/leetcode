# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
            

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodes = [[root, 1]]
        res = 0
        while nodes:
            node, depth = nodes.pop()
            if node:
                res = max(res, depth)
            if node.left:
                nodes.append([node.left, depth + 1])
            if node.right:
                nodes.append([node.right, depth + 1])
        return res