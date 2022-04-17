# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    list_len = 0
    while head:
        list_len += 1
        head = head.next
    for i in range(list_len // 2):
        head = head.next
