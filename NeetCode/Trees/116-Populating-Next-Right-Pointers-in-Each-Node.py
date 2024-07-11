"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        while curr and curr.left:
            nextCurr = curr.left
            nextCurr.next = curr.right
            adjacent = curr.next
            nextCurr = nextCurr.next
            while adjacent and adjacent.left:
                nextCurr.next = adjacent.left
                nextCurr = nextCurr.next
                nextCurr.next = adjacent.right
                nextCurr = nextCurr.next 
                adjacent = adjacent.next
            curr = curr.left
        return root