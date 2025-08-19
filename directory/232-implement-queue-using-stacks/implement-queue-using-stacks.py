class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
    def peek(self) -> int:

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
    def empty(self) -> bool:
         return not self.stack1 and not self.stack2

    def emptyQueue(self) -> None:
        self.stack1.clear()  # Clears all elements in stack1
        self.stack2.clear()  # Clears all elements in stack2


#didnt understand
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.emptyQueue()  # Clears the queue
obj.push(6)
obj.push(7)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()