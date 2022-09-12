# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev, curr = None, head
#         while curr:
#             tmp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = tmp
#         return prev

# recursive
head = ListNode(1, ListNode(2, ListNode(3, None)))
def reverse_pointer(prev, curr):
    if curr == None:
        return prev
    else:
        tmp = curr.next
        curr.next = prev
        return reverse_pointer(curr, tmp)

ans = reverse_pointer(None, head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead