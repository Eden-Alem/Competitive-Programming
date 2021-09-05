class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myStack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.myStack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.myStack.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.myStack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if (len(self.myStack) != 0):
            return False
        return True
        

