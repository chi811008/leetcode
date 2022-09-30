# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        
        def get_height(node):
            if node == None:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            diff = left_height - right_height
            if diff > 1 or diff < -1:
                res[0] = False

            height = 1 + max(left_height, right_height)
            return height
        
        get_height(root)
        return res[0]

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return True, 0
            left_balance, left_height = dfs(node.left)
            right_balance, right_height = dfs(node.right)
            balance = left_balance and right_balance and abs(left_height - right_height) <= 1
            
            return balance, 1 + max(left_height, right_height)
        
        balance, height = dfs(root)
        return balance