# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
   
        # get length
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        if k == 0:
            return head
        
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead