def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    ptr = head
    list_len = 0
    while ptr:
        list_len += 1
        ptr.next
    for i in range(list_len - 1):
        if i == n:
            