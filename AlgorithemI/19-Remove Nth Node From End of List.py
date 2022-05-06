head = [1,2,3,4,5]
n = 2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

fast = slow = dummy = head # [1, 2, 3, 4, 5]
for i in range(n):
    fast = fast.next # [3, 4, 5]

if fast is None:
    return head.next

while fast.next:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next
return dummy