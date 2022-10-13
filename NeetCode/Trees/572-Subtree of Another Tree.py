# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        
        if self.same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def same_tree(self, t, s):
        if t == None and s == None:
            return True
        
        if t and s and (t.val == s.val):
            left_same = self.same_tree(t.left, s.left)
            right_same = self.same_tree(t.right, s.right)
            return left_same and right_same
        return False