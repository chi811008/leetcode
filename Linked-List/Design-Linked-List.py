class Node:
    def __init__(self, val=0, nextN=None):
        self.val = val
        self.next = nextN


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        

    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr and curr != self.tail else -1


    def addAtHead(self, val: int) -> None:
        nextN = self.head.next
        newNode = Node(val, nextN)
        self.head.next = newNode
        

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr and (curr.next != self.tail):
            curr = curr.next
        newNode = Node(val, self.tail)
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        while curr and (index > 0):
            curr = curr.next
            index -= 1
        
        if index == 0 and curr and curr != self.tail:
            nextN = curr.next
            newNode = Node(val, nextN)
            curr.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        prev = self.head
        while curr and (index > 0):
            prev = curr
            curr = curr.next
            index -= 1
        
        if index == 0 and curr and curr != self.tail:
            # delete curr
            prev.next = curr.next
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)