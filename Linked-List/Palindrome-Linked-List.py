# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# extra memory
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        h, t = 0, len(vals)-1
        while t > h:
            if vals[h] != vals[t]:
                return False
            h += 1
            t -= 1
        
        return True

# Space Complexity = O(1)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow
        while curr:
            nextCurr = curr.next
            curr.next = prev
            prev = curr
            curr = nextCurr
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True