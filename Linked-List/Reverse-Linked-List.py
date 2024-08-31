# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionRecursive:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head or not head.next:
			return head
		new_head = self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return new_head


class SolutionIterative:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev = None
		curr = head
		while curr:
			nextCurr = curr.next
			curr.next = prev
			prev = curr
			curr = nextCurr
		return prev
      
