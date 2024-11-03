# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return

        stack = []
        res = []

        def traverseLeft(node):
            if node is None:
                return
            while node:
                stack.append(node)
                node = node.left
            return

        traverseLeft(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                traverseLeft(node.right)
        return res
