class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minStack) == 0):
            self.minStack.append(val)
        else:
            if (self.minStack[-1] > self.stack[-1]):
                self.minStack.append(self.stack[-1])
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:        
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()