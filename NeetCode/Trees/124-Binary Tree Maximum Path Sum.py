# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = [root.val]
        def dfs(node):
            if node == None:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            node_max = max(node.val, node.val + left_max + right_max, node.val + left_max, node.val + right_max)
            max_val[0] = max(max_val[0], node_max)
            return max(node.val, node.val + left_max, node.val + right_max)
        dfs(root)
        return max_val[0]