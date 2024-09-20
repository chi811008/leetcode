# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traverse(node):
            if not node:
                return
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return res
        
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        res = []
        
        stack = [root]
                
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res