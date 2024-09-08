# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        add1 = 0
        dummy = curr = ListNode()
        while curr1 or curr2 or add1:
            curr1Val = curr1.val if curr1 else 0
            curr2Val = curr2.val if curr2 else 0
            
            newVal = curr1Val + curr2Val + add1
            
            curr.next = ListNode(newVal % 10)
            add1 = newVal // 10
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            curr = curr.next
        return dummy.next