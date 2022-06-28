# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    fast, slow = head
    while fast:
        fast = fast.next.next
        slow = slow.next
    return slow
    






# 1. count len
def middleNode(head):
    linked_len = 0
    _ = head
    while _ is not None:
        linked_len += 1
        _ = _.next
    for i in range(linked_len // 2):
        head = head.next

# 2. use two pointer
def middleNode(head):
    fast = head
    slow = head
    while (fast and fast.next):
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        return slow.next
    return slow