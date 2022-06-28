def rev(head, prev):
    if not head:
        return prev
    nxt = head.next
    head.next = prev
    return rev(nxt, head)
    
rev(head, None)