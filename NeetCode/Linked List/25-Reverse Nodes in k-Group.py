# Definition for singly-linked list.
from tokenize import group


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        
        while True:
            kth = self.get_kth(prev_group, k)
            if kth == None:
                break
            
            next_group = kth.next
            prev, curr = next_group, prev_group.next
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
            
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr
        
        
        
        