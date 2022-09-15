# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L, R = head, head
        for i in range(n):
            R = R.next
        if R == None:
            return head.next
        dummy = L
        while R.next:
            R = R.next
            L = L.next
        L.next = L.next.next
        return dummy