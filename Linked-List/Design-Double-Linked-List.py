class Node:
    def __init__(self, val, nextNode, prevNode):
        self.val = val
        self.next = nextNode
        self.prev = prevNode
        
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(0, self.tail, None)
        self.tail = Node(0, None, self.head)
        self.head.next = self.tail

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr and curr != self.tail:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        nextNode = self.head.next
        prevNode = self.head
        newNode = Node(val, nextNode, prevNode)
        prevNode.next = newNode
        nextNode.prev = newNode

    def addAtTail(self, val: int) -> None:
        nextNode = self.tail
        prevNode = self.tail.prev
        newNode = Node(val, nextNode, prevNode)
        prevNode.next = newNode
        nextNode.prev = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr and curr != self.tail:
            nextNode = curr.next
            prevNode = curr
            newNode = Node(val, nextNode, prevNode)
            prevNode.next = newNode
            nextNode.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            nextNode = curr.next
            prevNode = curr.prev
            prevNode.next = nextNode
            nextNode.prev = prevNode
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)