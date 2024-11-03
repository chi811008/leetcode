from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# top down
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if node is None:
                return depth
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 0)


# bottom up
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Time complexity: O(n)
# Space complexity: O(n)


def runTest():
    test = Solution()
    print(test.maxDepth([3, 9, 20, None, None, 15, 7]))  # 3
    print(test.maxDepth([1, None, 2]))  # 2
    print(test.maxDepth([]))  # 0
    print(test.maxDepth([0]))  # 1


if __name__ == "__main__":
    runTest()
