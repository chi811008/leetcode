# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node == None:
                return 0
            if node.val >= max_val:
                max_val = node.val
                return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)
            return dfs(node.left, max_val) + dfs(node.right, max_val) 

        return dfs(root, root.val)