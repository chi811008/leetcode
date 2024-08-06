class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.storage = [-1] * k
        self.head, self.tail = -1, -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        
        self.tail = (self.tail + 1) % self.k
        self.storage[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.storage[self.head] = -1
        if self.head == self.tail:
            self.head, self.tail = -1, -1
        else:
            self.head = (self.head + 1) % self.k
        return True
        
    
    def Front(self) -> int:
        return self.storage[self.head] if self.head != -1 else -1
        

    def Rear(self) -> int:
        return self.storage[self.tail] if self.tail != -1 else -1
        

    def isEmpty(self) -> bool:
        return self.head == -1


    def isFull(self) -> bool:
        return ((self.tail + 1) % self.k) == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()