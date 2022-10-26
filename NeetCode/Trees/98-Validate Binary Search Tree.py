# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_valid(node, lower_bound, upper_bound):
            if node == None:
                return True
            if not (lower_bound < node.val and node.val < upper_bound):
                return False
            return check_valid(node.left, lower_bound, node.val) and check_valid(node.right, node.val, upper_bound)
        return check_valid(root, -float("inf"), float("inf"))