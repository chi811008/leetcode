# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        
        # preorder traversal
        if p.val == q.val:
            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)
            return left_same and right_same
        return False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)