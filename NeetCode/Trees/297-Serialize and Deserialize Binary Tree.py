# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """ 
        res = list()
        def preorder_traversal_dfs(node):
            if node == None:
                res.append("null")
            else:
                res.append(str(node.val))
                preorder_traversal_dfs(node.left)
                preorder_traversal_dfs(node.right)
        preorder_traversal_dfs(root)
        return ",".join(res)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i = 0
        def preorder_build_tree():
            root_val = data[self.i]
            if root_val == "null":
                self.i += 1
                return None
            root = TreeNode(int(root_val))
            self.i += 1
            root.left = preorder_build_tree()
            root.right = preorder_build_tree()
            return root
        return preorder_build_tree()
