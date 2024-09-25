class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = []


    def push(self, val: int) -> None:
        minIndex = self.minIndex[-1] if self.minIndex else 0
        if self.stack and self.stack[minIndex] > val:
            minIndex = len(self.stack)

        self.stack.append(val)
        self.minIndex.append(minIndex)
        return
        

    def pop(self) -> None:
        self.stack.pop()
        self.minIndex.pop()
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.minIndex[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()