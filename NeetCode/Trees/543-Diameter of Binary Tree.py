# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]        
        def get_height(node):
            if node == None:
                return -1
        
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            diameter = left_height + right_height + 2
            res[0] = max(res[0], diameter)

            height = 1 + max(left_height, right_height)
            return height
        get_height(root)
        return res[0]
