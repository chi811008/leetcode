class MinStack:
    def __init__(self):
        self.container = list()
        self.min_val = None

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val) if self.min_val else val
        self.container.append(val)

    def pop(self) -> None:
        val = self.container.pop()
        if self.container and val == self.min_val:
            self.min_val = min(self.container)
        
    def top(self) -> int:
        return self.container[-1]
        
    def getMin(self) -> int:
        return self.min_val
        